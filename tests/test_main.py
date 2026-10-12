import runpy
from pathlib import Path


def test_bloco_principal_executa(capsys):
    caminho = Path(__file__).resolve().parent.parent / "fincalc.py"
    runpy.run_path(str(caminho), run_name="__main__")
    saida = capsys.readouterr().out
    assert "Iniciando o sistema FinCalc..." in saida
    assert "Juros Simples: R$ 1100.00" in saida
