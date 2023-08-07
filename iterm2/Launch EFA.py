import iterm2

tab_title = "EFA"
color = iterm2.Color(13, 71, 161) # Material Blue 900
panes = [
    { 
      "title": "React Web Client",
      "path": "~/dev/edvisor/react-web-client",
      "scripts": ["nvm use", "yarn storybook"]
    },
    { 
      "title": "V2",
      "path": "~/dev/edvisor/api-server-v2/v2",
      "scripts": ["nvm use", "yarn dev"]
    },
    { 
      "title": "V1",
      "path": "~/dev/edvisor/api-server-v2/v1",
      "scripts": ["nvm use", "git pull", "yarn dev"]
    },
    { 
      "title": "Web Client",
      "path": "~/dev/edvisor/web-client",
      "scripts": ["nvm use", "git pull"]
    },
    { 
      "title": "i18n",
      "path": "~/dev/edvisor/i18n",
      "scripts": ["nvm use", "git pull", "yarn dev"]
    }
]

change = iterm2.LocalWriteOnlyProfile()
change.set_tab_color(color)
change.set_use_tab_color(True)

async def create_pane(tab, pane, index):
    title = pane["title"]
    path = pane["path"]
    scripts = pane["scripts"]
    # Create a new session in the current tab
    session = tab.current_session

    # Set the tab color
    await session.async_set_profile_properties(change)

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

    # Create panes in the new tab
    for index, pane in enumerate(panes):
        print(f"Creating pane {index + 1} with path: {pane['path']}")
        await create_pane(tab, pane, index)

    tab.async_set_title(tab_title)

iterm2.run_until_complete(main)
