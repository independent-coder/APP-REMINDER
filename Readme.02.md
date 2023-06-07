1. Import Statements:
   - Removed the import statement for `ttk`.
   - Removed the import statement for `messagebox`.

2. Root Geometry and Icon:
   - Changed the root geometry to "265x357" to fit the updated layout.
   - Set a custom icon for the root window using the `iconbitmap()` method.

3. Reminder Limit:
   - Added a `max_reminders` attribute to limit the number of reminders to 5.
   - Added a check to see if the number of reminders exceeds the limit before adding a new reminder.

4. Styling Changes:
   - Modified the background color (`bg`) and foreground color (`fg`) of various labels, buttons, and frames to achieve a consistent dark color scheme.
   - Set a border (`bd`) and relief (`relief`) for the reminder frames.

5. Event and Time Entry Validation:
   - Added validation functions for the event and time entries to limit the maximum number of characters allowed.

6. Error Handling:
   - Modified the `show_error()` method to display error messages in a separate top-level window with a custom background color and icon.

7. Countdown Label:
   - Added a countdown label to each reminder frame to display the remaining time until the event.
   - Stored the countdown label as a reference in the `reminder` dictionary for easy access.

8. Reminder Cancellation:
   - Added a `canceled` key to the `reminder` dictionary to keep track of canceled reminders.
   - Implemented the `cancel_reminder()` method to remove a reminder when the cancel button is clicked.
   - Destroyed the reminder frame and removed the reminder from the events list when canceled.

9. Time Comparison and Days Countdown:
   - Modified the `start_countdown()` method to compare the current time with the reminder time using the `>=` operator.
   - Implemented a days countdown feature that decreases the number of days until the event by subtracting 1 at midnight (0:00).

10. Reminder Popup Styling:
    - Modified the background color (`bg`) and text color (`fg`) of the reminder popup window.
    - Set the font and color of the event label in the popup window.

11. Additional Changes:
    - Set a consistent background color for the root window and reminders frame.

12. Maximum char:
   - A maximum character for event and time was added

13. Deleted ScrollBar:
    -The scroll bar was bugging so i deleted it.
    -So i add a maximum of event of 5.


Thank you for everything
Please star my project!

[Screenshot_31](https://github.com/independent-coder/APP-REMINDER/assets/127637860/f5a0e04b-3113-4c6a-bd74-8c3880018bb3)

![Screenshot_30](https://github.com/independent-coder/APP-REMINDER/assets/127637860/0e985591-f3a3-4c8a-9c7e-31f01f70efc2)

![Screenshot_29](https://github.com/independent-coder/APP-REMINDER/assets/127637860/935616c4-33c0-4632-919c-7f80c9ae31fe)

![Screenshot_28](https://github.com/independent-coder/APP-REMINDER/assets/127637860/ef3c4140-f32a-4792-aac8-df158ab47436)


