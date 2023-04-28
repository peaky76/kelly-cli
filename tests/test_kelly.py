from click.testing import CliRunner
from kelly_cli.kelly import kelly


def test_decimal():
    runner = CliRunner()
    result = runner.invoke(kelly, ["4", "5"])
    assert result.exit_code == 0
    assert "£6.25" in result.output


def test_probability_abbr():
    runner = CliRunner()
    result = runner.invoke(kelly, ["-p", "0.25", "0.2"])
    assert result.exit_code == 0
    assert "£6.25" in result.output


def test_probability_full():
    runner = CliRunner()
    result = runner.invoke(kelly, ["--prob", "0.25", "0.2"])
    assert result.exit_code == 0
    assert "£6.25" in result.output


def test_percentage_abbr():
    runner = CliRunner()
    result = runner.invoke(kelly, ["-c", "25", "20"])
    assert result.exit_code == 0
    assert "£6.25" in result.output


def test_percentage_full():
    runner = CliRunner()
    result = runner.invoke(kelly, ["--percent", "25", "20"])
    assert result.exit_code == 0
    assert "£6.25" in result.output


def test_bank():
    runner = CliRunner()
    result = runner.invoke(kelly, ["4", "5", "-b", "200"])
    assert result.exit_code == 0
    assert "£12.50" in result.output


def test_commission():
    runner = CliRunner()
    result = runner.invoke(kelly, ["4", "6", "-b", "200", "-m", "20"])
    assert result.exit_code == 0
    assert "£12.50" in result.output


def runner():
    test_decimal()
    test_probability_abbr()
    test_probability_full()
    test_percentage_abbr()
    test_percentage_full()
    test_bank()
    test_commission()
    print("7 tests passed successfully")
