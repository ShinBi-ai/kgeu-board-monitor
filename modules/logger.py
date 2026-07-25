from datetime import datetime


class Logger:
    @staticmethod
    def _log(level: str, message: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{now}] [{level}] {message}")

    @staticmethod
    def info(message: str):
        Logger._log("INFO", message)

    @staticmethod
    def success(message: str):
        Logger._log("SUCCESS", message)

    @staticmethod
    def warning(message: str):
        Logger._log("WARNING", message)

    @staticmethod
    def error(message: str):
        Logger._log("ERROR", message)

    @staticmethod
    def banner():
        print("=" * 60)
        print("KGEU BOARD MONITOR")
        print("=" * 60)