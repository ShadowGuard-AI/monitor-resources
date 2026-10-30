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

- `--interval`: Time interval (in seconds) between resource checks. Default is 5 seconds.
- `--threshold`: Threshold (in percentage) for alerts. Default is 90%.

On every check the tool logs CPU, memory, and disk usage, and warns when a value exceeds the threshold. It runs until interrupted (Ctrl+C). Note that importing main.py creates a `monitor_resources.log` file in the working directory.

### Security Warnings

This tool is intended for system monitoring and analysis. It does not provide any security features or protection.

### License

This project is licensed under the GNU General Public License v3.0, and is licensed to CY83R-3X71NC710N.