// Form1.cs
using System;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;

namespace AlarmClockForm
{
    public partial class Form1 : Form
    {
        // Define delegate and event
        public delegate void AlarmEventHandler(object source, EventArgs args);
        public event AlarmEventHandler RaiseAlarm;

        private DateTime targetTime;
        private bool isRunning = false;
        private Thread monitorThread;
        private Random random = new Random();

        public Form1()
        {
            InitializeComponent();
            RaiseAlarm += Ring_Alarm;
        }

        // Handle button click event
        private void btnStart_Click(object sender, EventArgs e)
        {
            if (isRunning)
            {
                MessageBox.Show("Alarm is already running!", "Warning",
                    MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            string inputTime = txtTime.Text;
            DateTime parsedTime;

            // Validate input time format
            if (DateTime.TryParseExact(inputTime, "HH:mm:ss", null,
                System.Globalization.DateTimeStyles.None, out parsedTime))
            {
                // Create a new DateTime with today's date and input time
                DateTime today = DateTime.Today;
                targetTime = new DateTime(
                    today.Year,
                    today.Month,
                    today.Day,
                    parsedTime.Hour,
                    parsedTime.Minute,
                    parsedTime.Second
                );

                // If the target time is already past for today, show an error
                if (targetTime < DateTime.Now)
                {
                    MessageBox.Show("This time has already passed today. Please enter a future time.",
                        "Invalid Time", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                // Start monitoring
                StartMonitoring();
            }
            else
            {
                MessageBox.Show("Invalid format. Please use HH:MM:SS format.",
                    "Format Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void StartMonitoring()
        {
            isRunning = true;
            lblStatus.Text = "Monitoring... Target: " + targetTime.ToString("HH:mm:ss");

            // Disable input during monitoring
            txtTime.Enabled = false;
            btnStart.Enabled = false;

            // Start checking the time in a separate thread
            monitorThread = new Thread(MonitorTime);
            monitorThread.IsBackground = true;  // Make it a background thread
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
                    // Invoke the event on the UI thread
                    this.Invoke(new Action(() =>
                    {
                        OnRaiseAlarm();
                        isRunning = false;

                        // Re-enable input
                        txtTime.Enabled = true;
                        btnStart.Enabled = true;
                        lblStatus.Text = "Alarm triggered!";
                    }));

                    return;
                }

                // Change form background color every second
                this.Invoke(new Action(() =>
                {
                    this.BackColor = GetRandomColor();
                }));

                // Check every second
                Thread.Sleep(1000);
            }
        }

        private Color GetRandomColor()
        {
            return Color.FromArgb(
                random.Next(100, 256),  // Red component
                random.Next(100, 256),  // Green component
                random.Next(100, 256)   // Blue component
            );
        }

        // Method to trigger the alarm event
        protected virtual void OnRaiseAlarm()
        {
            if (RaiseAlarm != null)
            {
                RaiseAlarm(this, EventArgs.Empty);
            }
        }

        // Event handler for the alarm
        private void Ring_Alarm(object source, EventArgs e)
        {
            MessageBox.Show("ALARM! The time is now: " + DateTime.Now.ToString("HH:mm:ss"),
                "Alarm Triggered", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        // Clean up when form is closing
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            isRunning = false;
            if (monitorThread != null && monitorThread.IsAlive)
            {
                // Give the thread time to exit cleanly
                monitorThread.Join(1000);
            }
        }

        private void lblInstructions_Click(object sender, EventArgs e)
        {

        }

        private void lblStatus_Click(object sender, EventArgs e)
        {

        }
    }
}