# File Processing App

## 📄 Description
The File Processing App is a Rust application example that reads data from a file, processes it, and captures and sends errors to Sentry for error tracking. 

The application utilizes the Sentry, Redis, and PostgreSQL stack for error handling and monitoring.

## ⚙️ App Details

| Language | Frameworks | All-In Toolset Part |
|-----------|---------------------|---------------------|
| Rust | - | Sentry + Redis + PostgreSQL |

## 🚀 Prerequisites
To run this application, you'll need the following:
- Rust installed on your machine ([Installation Guide](https://www.rust-lang.org/tools/install))
- DSN (Data Source Name) for error tracking from Sentry installation

## 📖 Usage
1. Clone this repository or download the source code.
2. Set the `SENTRY_DSN` environment variable to your Sentry DSN.
3. Install the required dependencies and build the application by running `cargo build`.
4. Run the application using `cargo run`.
5. The application will read data from the `data.txt` file and process it.
6. If any errors occur during the data processing, they will be captured and sent to Sentry for error tracking.
7. Optional: To simulate the "no file" error and test the error tracking functionality accurately, do not create the file that the application is expected to process.

## 📄 License
This project is licensed under the [MIT License](../../LICENSE).

---

```python
< 🏆 Happy BunnyShelling 🚀 >
-----------------------------
              \
               \   
                      .".
                     /  |
                    /  /
                   / ,"
       .-------.--- /
      "._ __.-/ o. o\
         "   (    Y  )
              )     /
             /     (
            /       Y
        .-"         |
       /  _     \    \
      /    `. ". ) /' )
     Y       )( / /(,/
    ,|      /     )
   ( |     /     /
    " \_  (__   (__        
        "-._,)--._,)
```
