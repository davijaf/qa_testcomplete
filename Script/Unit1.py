def Login():
    Browsers.Item[btChrome].Navigate(Project.Variables.envURL)
    Aliases.browser.pageShop.Wait()
    Aliases.browser.BrowserWindow.Maximize()
    Aliases.browser.pageShop.header.navUsd.linkLogIn.textnodeLogIn.Click()
    Aliases.browser.pageLogin.Wait()
    Aliases.browser.pageLogin.sectionContent.textboxUsernameoremail.Click()
    Aliases.browser.pageLogin.sectionContent.textboxUsernameoremail.SetText("davijaf")
    Aliases.browser.pageLogin.sectionContent.passwordboxPassword.Click()
    Aliases.browser.pageLogin.sectionContent.passwordboxPassword.SetText(Project.Variables.Password1)
    Aliases.browser.pageLogin.sectionContent.buttonLogIn.ClickButton()
    

def Logout():
  Browsers.Item[btChrome].Navigate("https://services.smartbear.com/samples/TestComplete12/smartstore/")
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  link = browser.pageShop.header.navUsd
  Aliases.browser.pageLogin.sectionContent.link.linkDavijaf.textnode.Click()
  Aliases.browser.pageLogin.sectionContent.link.linkLogOut.textnodeLogOut.Click()
