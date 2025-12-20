# MongoDB Installation on Windows (with MongoDB Shell)

This guide explains how to install **MongoDB Community Server** and the **MongoDB Shell (`mongosh`)** on Windows.

> Note: Steps may vary slightly between versions of Windows and MongoDB. Refer to the official MongoDB documentation for any changes.[web:20]

---

## 1. Download MongoDB Community Server

1. Go to the official MongoDB **Download Center** in your browser.[web:20]  
2. Select:
   - Edition: *Community Server*  
   - Platform: *Windows*  
   - Package: *MSI* installer[web:20]  
3. Click **Download** to get the installer file.[web:20]

---

## 2. Run the MongoDB Installer

1. Double-click the downloaded `.msi` file to start the setup wizard.[web:14]  
2. Accept the license agreement and choose **Complete** setup.[web:14]  
3. When asked about configuration:
   - Select **Run service as Network Service user** (default)  
   - Keep the default data directory (e.g., `C:\Program Files\MongoDB\Server\<version>\`) unless you have special needs[web:14]  
4. Finish the installer; MongoDB Server will be installed as a Windows service and set to start automatically.[web:11][web:14]

---

## 3. Install MongoDB Shell (mongosh)

Recent MongoDB Community Server installers may include **mongosh**; if not, install it separately.

1. Download **MongoDB Shell (mongosh)** from the official MongoDB download page (Shell section).[web:20]  
2. Choose:
   - Platform: *Windows*  
   - Package: Installer (`.msi`) or ZIP archive[web:20]  
3. Run the `.msi` installer or extract the ZIP to a folder such as `C:\Program Files\mongosh\`.  

---

## 4. Add MongoDB and mongosh to PATH

To use `mongod` and `mongosh` from any terminal, add them to your system `PATH`.

1. Locate:
   - MongoDB Server `bin` directory, e.g.  
     `C:\Program Files\MongoDB\Server\<your_version>\bin`  
   - `mongosh` directory, e.g.  
     `C:\Program Files\mongosh\` or wherever you installed it[web:11][web:14]  
2. Open **Start Menu → search “Environment Variables” → Edit the system environment variables**.  
3. Click **Environment Variables…**.  
4. Under **System variables**, select `Path` → **Edit**.  
5. Click **New** and add:
   - `C:\Program Files\MongoDB\Server\<your_version>\bin`  
   - The folder where `mongosh.exe` resides[web:11][web:14]  
6. Click **OK** on all dialogs to save.

Close and reopen any Command Prompt or PowerShell windows so the new `PATH` is loaded.

---

## 5. Verify Installation

Open **Command Prompt** or **PowerShell** and run:

```mongod --version```


You should see version information for the MongoDB server.[web:11][web:14]

Then verify the shell:

```mongod --version```


You should see version information for `mongosh`.[web:13][web:20]

---

## 6. Start MongoDB and Connect with mongosh

If MongoDB was installed as a Windows service (default for the MSI installer), it should already be running.[web:11][web:14]

To confirm the service:

1. Open **Services** (search “Services” in Start Menu).  
2. Look for **MongoDB** in the list and confirm it is **Running** and set to **Automatic**.[web:14]

Now connect using `mongosh`:

```mongosh```


This will connect to the default `mongodb://127.0.0.1:27017` instance and drop you into an interactive MongoDB shell.[web:13][web:20]

---

## 7. Basic Test Commands in mongosh

Run a few simple commands after `mongosh` connects:

// Show databases

``show dbs``

// Switch to a test database

``use test``

// Insert a document

``db.sample.insertOne({ name: "test-doc", createdAt: new Date() })``

// Query documents

``db.sample.find()``

If these commands run without errors and you see your inserted document, MongoDB and `mongosh` are working correctly.[web:13][web:20]

---

## 8. Uninstall or Upgrade

- To **uninstall**, use **Apps & Features** in Windows and remove **MongoDB Community Server** and **MongoDB Shell**.[web:14]  
- To **upgrade**, download a newer MSI from the MongoDB Download Center and run the installer, following the same steps as above.[web:20]

For advanced configuration (custom data directories, replication, authentication, etc.), refer to the official MongoDB manual.[web:20]
