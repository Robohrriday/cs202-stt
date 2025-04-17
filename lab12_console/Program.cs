using System;
using System.Threading;

namespace AlarmClock
{
    // Define the delegate for the alarm event
    public delegate void AlarmEventHandler(object source, EventArgs args);

    // Publisher class
    public class AlarmClock
    {
        // Declare the event using the delegate
        public event AlarmEventHandler RaiseAlarm;

        private DateTime targetTime;
        private bool isRunning = false;

        // Method to set the alarm time
        public void SetAlarm(DateTime time)
        {
            targetTime = time;
        }

        // Method to start checking the time
        public void Start()
        {
            isRunning = true;
            Console.WriteLine("Alarm set for: " + targetTime.ToString("HH:mm:ss"));
            Console.WriteLine("Monitoring time...");

            // Start checking the time
            Thread monitorThread = new Thread(MonitorTime);
            monitorThread.Start();
        }

        private void MonitorTime()
        {
            while (isRunning)
            {
                DateTime currentTime = DateTime.Now;

                // Check if current time matches target time
                if (currentTime.Hour == targetTime.Hour &&
                    currentTime.Minute == targetTime.Minute &&
                    currentTime.Second == targetTime.Second)
                {
                    // Trigger the event
                    OnRaiseAlarm();
                    isRunning = false;
                }

                // Check every second
                Thread.Sleep(1000);
            }
        }

        // Method to trigger the alarm event
        protected virtual void OnRaiseAlarm()
        {
            if (RaiseAlarm != null)
            {
                RaiseAlarm(this, EventArgs.Empty);
            }
        }
    }

    // Subscriber class
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Alarm Clock Application");
            Console.WriteLine("======================");

            // Create an instance of the alarm clock
            AlarmClock alarm = new AlarmClock();

            // Subscribe to the alarm event
            alarm.RaiseAlarm += Ring_Alarm;

            // Get time from user
            DateTime targetTime;

            while (true)
            {
                Console.Write("Enter alarm time (HH:MM:SS): ");
                string inputTime = Console.ReadLine();

                if (DateTime.TryParseExact(inputTime, "HH:mm:ss", null,
                    System.Globalization.DateTimeStyles.None, out targetTime))
                {
                    // Create a new DateTime with today's date and input time
                    DateTime today = DateTime.Today;
                    targetTime = new DateTime(
                        today.Year,
                        today.Month,
                        today.Day,
                        targetTime.Hour,
                        targetTime.Minute,
                        targetTime.Second
                    );

                    // If the target time is already past for today, prompt again
                    if (targetTime < DateTime.Now)
                    {
                        Console.WriteLine("This time has already passed today. Please enter a future time.");
                        continue;
                    }

                    break;
                }
                else
                {
                    Console.WriteLine("Invalid format. Please use HH:MM:SS format.");
                }
            }

            // Set and start the alarm
            alarm.SetAlarm(targetTime);
            alarm.Start();

            // Keep the application running
            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }

        // Event handler for the alarm
        static void Ring_Alarm(object source, EventArgs e)
        {
            Console.WriteLine("\nALARM! ALARM! ALARM!");
            Console.WriteLine("The time is now: " + DateTime.Now.ToString("HH:mm:ss"));
            Console.WriteLine("Wake up!");
        }
    }
}