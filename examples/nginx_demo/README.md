# Nginx Demo

## 📄 Description
The Nginx Demo is a simple example that runs a local Nginx demo server and then exposes it to the internet using tunneling tools.

## ⚙️ App Details

| Language | Frameworks | All-In Toolset Part |
|-----------|---------------------|---------------------|
| - | - | Chisel + Hoppscotch |

## 🚀 Prerequisites
To run this application, you'll need the following:
- Docker installed in your machine ([Installation Guide](https://docs.docker.com/engine/install/))

## 📖 Usage
1. Expose the Nginx Demo app by running the following command: `docker run -p80:80 -d nginxdemos/hello`
2. Run the Chisel Client to establish the tunneling: 
```bash
docker run --rm -it --network=host jpillora/chisel client -v https://chisel-server-*****.bunnyenv.com R:30000:localhost:80
```
3. Access your locally shared app remotely:
```bash
curl https://chisel-tunnel-*****.bunnyenv.com
```

## 📄 License
This project is licensed under the [MIT License](../../LICENSE).

---

```python
< 🏆 Happy BunnyShelling 🚀 >
-----------------------------
          \
           \   
            \
                              .=""--._
                 __..._    ,="_`/.--""
            ..-""__...._"""       `^"\
          .'  ,/_,.__.- _,       _  .`.
        .'       _.' .-';       /_\ \o|_
      .'       -" .-'  /        `o' /   \,-
      `"""""----""    (        `.--'`---'='
                       `..     .'.`-..-/`\
                          `";`7 'j`"--'
                          _.| |  |
                       .-'    ;  `.
                    .-'  .-   :`   ;
                 .-'_.._7___ _7   ;|.---.
                (           `"\  /--..r=`)
                 \__..--"7'`. ,`7     `}\'
       __.    .-"       /    J/}/
   .-""   \.-"        .'     `;
  :      .'         .'       ;
  ;     /          :         |       .-._
  `.   :           |         ;-.    /`. `/
    `--|           ;        /   \  ;`. ` :
      _;           ;      .'     : :  .-':
    .' \          ;  _.--'       :/ .'  /
    |  ,__     .-'"""""--.       7 /   /
    :    \`""""           `.    ' /   /
     :    J__..._           `.   ;  .'
      \    -. `-.\            `,J.-'
       `._   `._.'                   
          `""""
```

