import papermill as pm
import importlib.resources as pkg_resources
import argparse
import sys

def execute_diagnostic(output_path):
    # Dynamically locate the notebook
    notebook_resource = pkg_resources.files('atw_diags').joinpath('notebooks', 'atw_atmos_ts_monthly_sfc_ocean.ipynb')
    
    print(f"Found template notebook at: {notebook_resource}")
    print(f"Executing and saving to: {output_path}")

    # Extract and run
    with pkg_resources.as_file(notebook_resource) as input_path:
        pm.execute_notebook(
            input_path=str(input_path),
            output_path=output_path,
            kernel_name='spear-analysis',
        )

def execute_diagnostic_cli():
    """Wrapper for the command-line entry point."""
    parser = argparse.ArgumentParser(description="Run the ATW diagnostic notebook.")
    parser.add_argument("output", help="Path to save the executed notebook.")
    args = parser.parse_args()
    
    execute_diagnostic(args.output)

if __name__ == "__main__":
    # This allows it to be run via `python src/atw_diags/runner.py <output>` as well
    execute_diagnostic_cli()
