import click

from lightning_app.cli.cmd_apps import _AppManager
from lightning_app.cli.cmd_clusters import AWSClusterManager


@click.group(name="list")
def get_list():
    """List Lightning AI self-managed resources (clusters, etc…)"""
    pass


@get_list.command("clusters")
def list_clusters(**kwargs):
    """List your Lightning AI BYOC compute clusters."""
    cluster_manager = AWSClusterManager()
    cluster_manager.list()


@click.option(
    "--cluster-id",
    "cluster_id",
    type=str,
    required=False,
    default=None,
    help="Filter apps by associated Lightning AI compute cluster",
)
@get_list.command("apps")
def list_apps(cluster_id: str, **kwargs):
    """List your Lightning AI apps."""
    app_manager = _AppManager()
    app_manager.list(cluster_id=cluster_id)
