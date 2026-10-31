![Banner](banner.png)

## Monitor Resources

### Project Description

The `monitor-resources` tool allows you to track system resource usage. It provides a simple command-line interface to display real-time information on CPU, memory, and disk metrics.

### Installation

The tool is a single script (`main.py`) and is not published as a pip package. Clone this repository, then install its one third-party dependency, psutil (everything else it imports is in the Python standard library):

```
pip install psutil
```

### Usage Examples

To monitor system resource usage with the default settings (a check every 5 seconds, alerts above 90 percent), run:

```
python main.py
```

The only options main.py implements are:

```
python main.py --interval 10 --threshold 80
```

- `--interval`: Time interval (in seconds) between resource checks. Default is 5 seconds. It must be positive; a non positive interval exits with code 1 at startup.
- `--threshold`: Threshold (in percentage) for alerts. Default is 90 percent. It must be between 0 and 100; a value outside that range exits with code 1 at startup.

On every check the tool logs CPU usage, memory usage, and disk usage for every partition returned by `disk_partitions`, with the mountpoint named on each disk line, and warns when a value exceeds the threshold. It runs until interrupted (Ctrl+C). The `monitor_resources.log` file in the working directory is created only when monitoring starts, so a `--help` run creates no log file. The log file rotates at 1 MiB with 3 backup files kept, so the log and its backups are capped at about 4 MiB in total.

### Security Warnings

This tool is intended for system monitoring and analysis. It does not provide any security features or protection.

### License

This project is licensed under the GNU General Public License v3.0, and is licensed to CY83R-3X71NC710N.