using Microsoft.EntityFrameworkCore;

namespace webapi.Models
{
    public class MyDbContext : DbContext
    {
        public DbSet<TestGroup> TestGroups { get; set; }
        public DbSet<Test> Tests { get; set; }

        public string DbPath { get; }

        public MyDbContext()
        {
            var folder = Environment.SpecialFolder.LocalApplicationData;
            var path = Environment.GetFolderPath(folder);
            DbPath = Path.Join(path, "programmer-gpt.db");
        }

        // The following configures EF to create a Sqlite database file in the
        // special "local" folder for your platform.
        protected override void OnConfiguring(DbContextOptionsBuilder options)
            => options.UseSqlite($"Data Source={DbPath}", options => options.MigrationsAssembly("webapi"));
    }

    public class TestGroup
    {
        public int TestGroupId { get; set; }

        public List<Test> Tests { get; } = new();
    }

    public class Test
    {
        public int TestId { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }

        public int TestGroupId { get; set; }
        public TestGroup TestGroup { get; set; }
    }
}
