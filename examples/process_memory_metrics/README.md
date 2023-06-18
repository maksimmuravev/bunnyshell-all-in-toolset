# Bash Memory Monitoring Script

## 📄 Description
The Bash Memory Monitoring Script is a script example written in Bash that allows you to monitor the memory usage of a specific process. It can be useful for debugging memory leaks and analyzing memory usage patterns.

The script utilizes the Prometheus monitoring ecosystem, including Prometheus, Pushgateway, and Grafana, to collect, store, and visualize the memory metrics. It retrieves memory information using the `ps` and `vmmap` commands and sends the metrics to the Pushgateway, which can be scraped by Prometheus for monitoring and visualization in Grafana.

## ⚙️ App Details

| Language  | Framework | All-In Toolset Part      |
|-----------|-----------|-------------------------|
| Bash      | -         | Prometheus+Pushgateway+Grafana |


## 🚀 Prerequisites
To use this script, you'll need the following:
- Bash shell
- Process to investigate
- `ps` command for retrieving process memory information
- `vmmap` command for retrieving detailed memory maps

## ⚙️ Usage
1. Ensure you have the necessary dependencies installed, including ps, vmmap, and the required network tools for sending metrics.
2. Run the script using the following command:
```bash
bash run.sh <process_name>
```
Replace <process_name> with the name or command of the process you want to monitor.
3. The script will retrieve the memory metrics for the specified process and send them to the Pushgateway.

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

🏆 Happy BunnyShelling! 🏆


