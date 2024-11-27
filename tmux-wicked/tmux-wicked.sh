#!/bin/bash

LAYOUT_CONF="$HOME/.tmux-wicked/layout.conf"

if [[ -f $LAYOUT_CONF ]]; then
    source "$LAYOUT_CONF"
else
    echo "Layout configuration file not found!"
    exit 1
fi

# handle session creation
create_new_session() {
    session_name="session_$(date +'%m_%d_%H%M')"
    tmux new-session -d -s "$session_name"
    
    PS3="Select layout: "
    options=("T-shape" "M-shape" "Exit")
    select opt in "${options[@]}"; do
        case $REPLY in
            1) layout_T ;;
            2) layout_M ;;
            3) exit 0 ;;
            *) echo "Invalid option." ;;
        esac
        break
    done
    
    tmux attach -t "$session_name"
}

# attach to existing session
attach_to_existing_session() {
    echo "Available sessions:"
    select session_name in $sessions "Exit"; do
        if [[ "$session_name" == "Exit" ]]; then
            exit 0
        elif [[ -n "$session_name" ]]; then
            tmux attach -t "$session_name"
            break
        else
            echo "Invalid selection."
        fi
    done
}

# list existing sessions
list_sessions() {
    echo "Current tmux sessions:"
    echo "$sessions"
}

# kill existing session
kill_session() {
    echo "Available sessions:"
    select session_name in $sessions "Exit"; do
        if [[ "$session_name" == "Exit" ]]; then
            exit 0
        elif [[ -n "$session_name" ]]; then
            tmux kill-session -t "$session_name"
            echo "Session $session_name killed."
            break
        else
            echo "Emm.. something is wrong."
        fi
    done
}

# check for existing tmux sessions
sessions=$(tmux list-sessions -F "#S" 2>/dev/null)

# initial prompt based on number of sessions
if [[ -z "$sessions" ]]; then
    PS3="Select option: "
    options=("Create new session" "Exit")
    select opt in "${options[@]}"; do
        case $REPLY in
            1) create_new_session ;;
            2) exit 0 ;;
            *) echo "Invalid option." ;;
        esac
        break
    done
else
    PS3="Select option: "
    options=("List" "Attach" "Create" "Kill" "Exit")
    select opt in "${options[@]}"; do
        case $REPLY in
            1) list_sessions ;;  #just lists the sessions 
            2) attach_to_existing_session ;;
            3) create_new_session ;;
            4) kill_session ;;
            5) exit 0 ;;
            *) echo "Invalid option." ;;
        esac
    done
fi

