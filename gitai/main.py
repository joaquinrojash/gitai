import subprocess
import click
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from gitai.ai import generate_commit_message, generate_pr_description
from gitai.config import MAX_DIFF_CHARS

console = Console()

def get_staged_diff() -> str:
    result = subprocess.run(
        ["git", "diff", "--cached"],
        capture_output=True, text=True
    )
    return result.stdout

def get_full_diff() -> str:
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True, text=True
    )
    return result.stdout

def do_commit(message: str):
    result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        console.print("[green]✓ Committed successfully[/green]")
    else:
        console.print(f"[red]Commit failed:[/red] {result.stderr}")

@click.group()
def cli():
    """gitai — AI-powered git commit and PR assistant"""
    pass

@cli.command()
@click.option("--auto", "-a", is_flag=True, help="Stage all changes and commit without prompting")
@click.option("--dry-run", is_flag=True, help="Show the message but don't commit")
def commit(auto, dry_run):
    """Generate a commit message for your staged changes"""
    diff = get_staged_diff()

    if not diff:
        if auto:
            subprocess.run(["git", "add", "-A"])
            diff = get_staged_diff()
        else:
            console.print("[yellow]No staged changes found.[/yellow]")
            console.print("Stage your changes with [bold]git add[/bold] first, or use [bold]--auto[/bold] to stage all.")
            return

    if not diff:
        console.print("[red]Nothing to commit.[/red]")
        return

    diff = diff[:MAX_DIFF_CHARS]

    with console.status("[bold purple]Generating commit message...[/bold purple]"):
        message = generate_commit_message(diff)

    console.print(Panel(message, title="[bold]Suggested commit[/bold]", border_style="purple"))

    if dry_run:
        return

    if Confirm.ask("Use this message?"):
        do_commit(message)
    else:
        custom = click.prompt("Enter your own message (or press Ctrl+C to cancel)")
        do_commit(custom)

@cli.command()
@click.option("--base", default="main", help="Base branch to compare against")
def pr(base):
    """Generate a PR description comparing current branch to base"""
    result = subprocess.run(
        ["git", "diff", f"{base}...HEAD"],
        capture_output=True, text=True
    )
    diff = result.stdout

    if not diff:
        console.print(f"[yellow]No diff found against branch '{base}'.[/yellow]")
        return

    diff = diff[:MAX_DIFF_CHARS]

    with console.status("[bold purple]Generating PR description...[/bold purple]"):
        description = generate_pr_description(diff)

    console.print(Panel(description, title="[bold]PR description[/bold]", border_style="teal"))
    console.print("\n[dim]Copy the text above into your GitHub PR description.[/dim]")

def main():
    cli()

if __name__ == "__main__":
    main()