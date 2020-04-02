from config import config
import course_handler
from datetime import datetime
from models.course import Course
import notifier
import time

number = config['number']

notified = False

if __name__ == '__main__':
    watched_courses = list()

    for course in config['courses']:
       watched_courses.append(Course(course, '', '', (0, 0, 0, 0, 0, 0)))
       course_handler.update_class_info(watched_courses[-1])

    for course in watched_courses:
        course.seats = course_handler.get_seat_counts(course)
        print(f'[{datetime.now().strftime("%H:%M:%S")}] {course} is now being tracked!')
        notifier.send_sms(number, f'{course} is now being tracked!')
        notifier.notify_desktop(f'{course} is now being tracked!')

    while True:
        for course in watched_courses:
            print(f'[{datetime.now().strftime("%H:%M:%S")}] Now checking course: {course}')
            new_seats = course_handler.get_seat_counts(course)

            if new_seats == (-1, -1, -1, -1, -1, -1):
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Error checking course')
                if (not notified):
                    notifier.send_sms(number, f'ERROR CHECKING {course}!')
                    notified = True
                continue
            notified = False

            if new_seats != course.seats:
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Seats have changed! {course.seats} -> {new_seats}')

                course.seats = new_seats

                if int(new_seats[3]) > 0:
                    notifier.send_sms(number, f'{course} now has a waitlist seat!')
                    notifier.notify_desktop(f'{course} now has a waitlist seat!')
                if int(new_seats[0]) > 0:
                    notifier.send_sms(number, f'{course} now has seats!')
                    notifier.notify_desktop(f'{course} now has seats!')
                

        time.sleep(3)
