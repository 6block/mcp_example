from weather import mcp
def main():
    # Initialize and run mcp server
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
