using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace selenium_tests;

//
// Summary:
//      Provides Selenium first test
// Run:
//      dotnet test .\bin\Debug\net8.0\selenium_tests.dll --filter TestCategory="Selenium"
public class SeleniumTests
{
    [Test]
    [Category("Selenium")]
    public void FirstTest()
    {
        IWebDriver driver = new ChromeDriver();
        driver.Navigate().GoToUrl("https://www.selenium.dev/");
        Assert.That(driver.Title, Is.EqualTo("Selenium"));
        driver.Quit();
    }
}
