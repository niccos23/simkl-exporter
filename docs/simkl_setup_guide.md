# Simkl API Setup Guide 🔑

To use the Simkl Exporter, you need to authenticate securely with your Simkl account. This process involves getting three keys:

1.  **Client ID** (Public identifier for your app)
2.  **Client Secret** (Private password for your app)
3.  **Access Token** (The temporary key that grants access to your data)

Follow these steps to generate them.

---

## Step 1: Create a Simkl Developer App

To get a Client ID and Secret, you must register a "dummy" application on Simkl.

1.  Go to the [Simkl Developer Settings page](https://simkl.com/settings/developer/).
2.  Click the **"Create New App"** button.
3.  Fill in the form details:
    * **Name:** `Simkl Local Exporter` (or any name you like)
    * **Description:** `Backup tool` (doesn't matter)
    * **Website:** `http://localhost` (doesn't matter)
    * **Redirect URI:** ⚠️ **IMPORTANT: This must be exact** ⚠️
        ```
        http://localhost:8000/callback
        ```
        *(If this does not match exactly, the authorization script will fail.)*

4.  Click **Save**.
5.  You will now see your app listed. Click on its name to reveal your **Client ID** and **Client Secret**. Keep this tab open.

---

## Step 2: Configure your local environment

1.  In the root folder of the `simkl-exporter` project, create a new file named exactly `.env` (if it doesn't exist yet).
2.  Open the `.env` file in your text editor.
3.  Copy the **Client ID** and **Client Secret** from the Simkl website and paste them into the file like this:

    ```env
    SIMKL_CLIENT_ID=your_long_client_id_here
    SIMKL_CLIENT_SECRET=your_long_client_secret_here
    # Leave this empty for now, we will get it in the next step
    # SIMKL_ACCESS_TOKEN=
    ```
4.  **Save** the `.env` file.

---

## Step 3: Generate your Access Token

Now we will use the included helper script to perform the secure OAuth handshake.

1.  Make sure your terminal is open and your virtual environment is active `(.venv)`.
2.  Run the authorization script:
    ```bash
    python auth.py
    ```

3.  The script will print a long URL starting with https://simkl.com/oauth/authorize.... Copy and paste this URL into your web browser.
4.  You will be taken to Simkl's website. Log in if needed, and click **"Authorize"** to grant the app permission to read your data.
5.  IMPORTANT: After authorizing, Simkl will redirect you to http://localhost:8000/callback.

    Your browser will likely show an error page like "This site can't be reached" or "Unable to connect". This is normal and expected because nothing is running a web server on that port.
6.  Look at your browser's address bar at the top. You will see a URL that looks like this: http://localhost:8000/callback?code=SOME_VERY_LONG_MIXTURE_OF_LETTERS_AND_NUMBERS
7.  Copy just the long code part after the code= sign.
8.  Go back to your terminal. The script is waiting with a prompt: 3. Paste the code here and press Enter:.
9.  Paste the code you copied from the browser address bar and press Enter.
10. Look back at your terminal window. The script will have captured the handshake and printed your new Access Token.

    *Example terminal output:*
    ```text
    Authorization successful!
    Your ACCESS_TOKEN is:
    d7a8f8s7d6f87sd6f87s6d8f7s6d8f7...
    ```

---

## Step 4: Finalize the setup

1.  Copy that long **ACCESS_TOKEN** from your terminal window.
2.  Open your `.env` file again.
3.  Add the token to the file on a new line:

    ```env
    SIMKL_CLIENT_ID=your_long_client_id_here
    SIMKL_CLIENT_SECRET=your_long_client_secret_here
    SIMKL_ACCESS_TOKEN=d7a8f8s7d6f87sd6f87s6d8f7s6d8f7...
    ```

4.  **Save and close** the `.env` file.

**🎉 Success! You are now ready to run the main export script.**
