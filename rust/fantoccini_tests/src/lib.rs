#[cfg(test)]
mod tests {
    use fantoccini::{ClientBuilder, Locator};


    #[tokio::test]
    async fn web_test() {
        let url = "file:///C:/workspace/test-apps/web/v1/web-form.html";

        let mut cap = serde_json::map::Map::new();
        let opts = serde_json::json!({
            "args":[
                "--disable-search-engine-choice-screen"
            ]
        });
        cap.insert("goog:chromeOptions".to_string(), opts);

        let client = ClientBuilder::native()
            .capabilities(cap)
            .connect("http://localhost:9515")
            .await
            .expect("failed to connect to WebDriver");
        
        client.goto(&url).await.expect("failed to navigate to the test page");
        client.maximize_window().await.expect("failed to maximize window");
        let page_title = client.title().await.expect("failed to get page title");
        assert_eq!(page_title, "Web Form", "Page title does not match");

        let bio = client.find(Locator::Id("bio")).await.expect("failed to find element bio");
        bio.send_keys("test").await.expect("failed to send text to bio text-area");
        let submit = client.find(Locator::XPath("//button[text()='Submit']")).await.expect("failed to find element submit button");
        submit.click().await.expect("failed to click submit button");
        let message = client.find(Locator::Css("div.success-message")).await.expect("failed to find message element");
        let actual_message = message.text().await.expect("failed to get text for message element");
        assert_eq!(actual_message, "Success! Your form has been submitted.", "Message is not received");

        client.close().await.expect("failed to close the browser");

    }
}
