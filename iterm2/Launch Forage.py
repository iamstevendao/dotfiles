import iterm2

tab_title = "Forage"
color = iterm2.Color(27, 94, 32) # Material Green 900
panes = [
    { 
      "title": "Main App",
      "path": "~/dev/forage/forage",
      "scripts": ["meteor npm run start"]
    },
    { 
      "title": "Next",
      "path": "~/dev/forage/forage-next",
      "scripts": []
    },
]

async def create_pane(tab, pane, index):
    title = pane["title"]
    path = pane["path"]
    scripts = pane["scripts"]
    # Create a new session in the current tab
    session = tab.current_session

    # Determine split direction based on the index
    if index == 0:
        await session.async_split_pane(vertical=True)
    else:
        await session.async_split_pane()

    # Set the pane title
    await session.async_set_name(f'{tab_title} - {title}')

    # Set the pane directory
    await session.async_send_text(f'cd {path}\n')

    # Run the scripts in the pane
    for script in scripts:
        await session.async_send_text(f'{script}\n')

    # Print log for this pane
    print(f"Created pane {index + 1} with path: {path}")

async def main(connection):
    # Create a new tab
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    tab = await window.async_create_tab()
    session = tab.current_session

    # Set the tab color
    change = iterm2.LocalWriteOnlyProfile()
    change.set_tab_color(color)
    change.set_use_tab_color(True)
    await session.async_set_profile_properties(change)

    # Create panes in the new tab
    for index, pane in enumerate(panes):
        print(f"Creating pane {index + 1} with path: {pane['path']}")
        await create_pane(tab, pane, index)

    tab.async_set_title(tab_title)

iterm2.run_until_complete(main)
