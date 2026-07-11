# Google Analytics (GA4) Setup Guide

This document guides you step-by-step through setting up your Google Analytics 4 (GA4) property and replacing the placeholder in the code (`G-XXXXXXXXXX`) with your actual Measurement ID so you can start tracking visitors on your site.

## Step 1: Create a Google Analytics Account and Property

1. Go to [Google Analytics](https://analytics.google.com/) and sign in with your Google account.
2. If this is your first time, click **Start measuring**. If you already have an account, go to **Admin** (the gear icon in the bottom left corner) and click **Create Account** or **Create Property**.
3. Enter an **Account name** (e.g., "CCSE Quiz") and configure the data-sharing options as you prefer. Click **Next**.
4. In **Property setup**, enter a property name (e.g., "CCSE 2026 Web"), select your reporting time zone, and your currency. Click **Next**.
5. Answer the questions about your business/project and click **Create** (and accept the terms of service).

## Step 2: Create a Data Stream and Get the "Measurement ID"

1. After creating the property, you will be asked to choose a platform to collect data. Select **Web**.
2. Enter your website URL (e.g., `your-domain.com` or your GitHub Pages URL) and a stream name (e.g., "Main Web Traffic").
3. Make sure **Enhanced measurement** is toggled on.
4. Click **Create stream**.
5. You will now see your web stream details. In the top right corner, you will see your **MEASUREMENT ID**. This ID starts with the letter `G-` followed by a combination of numbers and letters (e.g., `G-1A2B3C4D5E`).
6. **Copy that Measurement ID**.

## Step 3: Replace the ID in the Code

1. Open the `index.html` file in a text editor.
2. Scroll down near the bottom of the file and locate the `loadGoogleAnalytics()` function.
3. You will see a line that looks like this:
   ```javascript
   const gaId = 'G-XXXXXXXXXX'; // REEMPLAZA ESTO CON TU ID DE MEDICIÓN (Measurement ID)
   ```
4. Replace `G-XXXXXXXXXX` with the Measurement ID you copied in Step 2. It will look something like this:
   ```javascript
   const gaId = 'G-1A2B3C4D5E';
   ```
5. Save the `index.html` file.

## Step 4: Verify!

1. Upload your updated `index.html` file to your web server (or GitHub).
2. Go to your website and click "Aceptar" on the cookie banner that appears at the bottom.
3. Go back to Google Analytics, select the **Realtime** tab on the left menu, and wait a few minutes. You should see at least 1 active user (you).

That's it! Google Analytics will now start tracking your visitor count, session duration, and much more.
