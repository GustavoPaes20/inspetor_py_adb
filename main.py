import subprocess
import datetime

def run_adb_command(command):
    try:
        resultado = subprocess.run(command, capture_output=True, text=True, shell=True)
        if resultado.stderr or resultado.returncode != 0:
            return None
        return resultado.stdout.strip()
    except:
        return None

def get_device_info():
    print("Coletando dados...")
    modelo = run_adb_command("adb shell getprop ro.product.model")
    versao_android = run_adb_command("adb shell getprop ro.build.version.release")
    bateria = run_adb_command("adb shell dumpsys battery | findstr level")
    
    report = f"""
    RELATÓRIO DO TESTE:
    Data/Hora: {datetime.datetime.now()}
    Modelo do Aparelho: {modelo.strip() if modelo else 'Nenhuma informação obtida'}
    Versão do Android: {versao_android.strip() if versao_android else 'Nenhuma informação obtida'}
    Status da Bateria: {bateria.strip() if bateria else 'Nenhuma informação obtida'}
    """

    print(report)
    
    with open("test_log.txt", "a") as f:
        f.write(report + "\n")
    print("Relatório salvo em test_log.txt")

if __name__ == "__main__":
    get_device_info()