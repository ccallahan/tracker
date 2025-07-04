"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import os
import PIL.Image
import requests
import staticmap
import PIL
import base64
from io import BytesIO

import reflex as rx

from rxconfig import config
from datetime import datetime


def calculate_schedule_diff(sch_time: str, est_time: str) -> int:
        # Calculate the difference between scheduled and estimated times
        scheduled = datetime.fromisoformat(sch_time)
        estimated = datetime.fromisoformat(est_time)
        diff = estimated - scheduled
        return int(diff.total_seconds() / 60)


class State(rx.State):
    """The app state."""

    data: str = ""
    img: str = ""

    @rx.event
    def get_train_status(self):
        """Get the train status."""
        curr_train: str = os.environ.get("CURRENT_TRAIN", "")
        gdq_active: str = os.environ.get("GDQ_ACTIVE", "false").lower()

        if gdq_active == "true":
            self.data = "Teebs and Chance are currently at GDQ! Please check back later for updates."
            return

        train_status = requests.get("https://api-v3.amtraker.com/v3/trains/"
                                    + curr_train)
        if train_status.status_code == 200:
            raw_train_data = train_status.json()
            train_data_root = next(iter(raw_train_data))
            train_data = raw_train_data[train_data_root][0]
            curr_station = train_data["eventCode"]
            curr_full_station = train_data["eventName"]
            lat = int(train_data["lat"])
            long = int(train_data["lon"])

            if curr_station == train_data["destCode"] and train_data["statusMessage"] == "SERVICE DISRUPTION":
                self.data = f"Teebs and Chance are somewhere on the rails, but Amtrak's tracking is not working due to a service disruption. Please check back later for updates."
                return

            for x in train_data["stations"]:
                if x["code"] == curr_station:
                    curr_status = str(x["status"]).lower()
                    curr_sch_dep = str(x["schDep"])
                    curr_dep = str(x["dep"])
                    curr_delay = calculate_schedule_diff(curr_sch_dep, curr_dep)


                    if train_data_root == "40":
                        on_time = 90
                    if train_data_root == "40":
                        on_time = 90
                        late = 91
                        horribly_late = 180
                        insanely_late = 240

                        if curr_status == "enroute":
                            if curr_delay <= on_time:
                                self.data = f"Teebs and Chance are on time! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= late:
                                self.data = f"Teebs and Chance are running late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                self.data = f"Teebs and Chance are horribly late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                self.data = f"Teebs and Chance are insanely late! They are currently {curr_status} to {curr_full_station}."

                        if curr_status == "station":
                            if curr_delay <= on_time:
                                self.data = f"Teebs and Chance are on time! They are currently at {curr_full_station}."
                            elif curr_delay <= late:
                                self.data = f"Teebs and Chance are running late! They are currently at {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                self.data = f"Teebs and Chance are horribly late! They are currently at {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                self.data = f"Teebs and Chance are insanely late! They are currently at {curr_full_station}."

                    if train_data_root == "1333":
                        on_time = 30
                        late = 31
                        horribly_late = 60
                        insanely_late = 90

                        if curr_status == "enroute":
                            if curr_delay <= on_time:
                                State.data = f"Teebs and Chance are on time! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= late:
                                State.data = f"Teebs and Chance are running late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                State.data = f"Teebs and Chance are horribly late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= insanely_late:
                                State.data = f"Teebs and Chance are insanely late! They are currently {curr_status} to {curr_full_station}."

                        if curr_status == "station":
                            if curr_delay <= on_time:
                                State.data = f"Teebs and Chance are on time! They are currently at {curr_full_station}."
                            elif curr_delay <= late:
                                State.data = f"Teebs and Chance are running late! They are currently at {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                State.data = f"Teebs and Chance are horribly late! They are currently at {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                State.data = f"Teebs and Chance are insanely late! They are currently at {curr_full_station}."

                    if train_data_root == "1340":
                        on_time = 30
                        late = 31
                        horribly_late = 60
                        insanely_late = 90

                        if curr_status == "enroute":
                            if curr_delay <= on_time:
                                State.data = f"Teebs and Chance are on time! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= late:
                                State.data = f"Teebs and Chance are running late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                State.data = f"Teebs and Chance are horribly late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                State.data = f"Teebs and Chance are insanely late! They are currently {curr_status} to {curr_full_station}."

                        if curr_status == "station":
                            if curr_delay <= on_time:
                                State.data = f"Teebs and Chance are on time! They are currently at {curr_full_station}."
                            elif curr_delay <= late:
                                State.data = f"Teebs and Chance are running late! They are currently at {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                State.data = f"Teebs and Chance are horribly late! They are currently at {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                State.data = f"Teebs and Chance are insanely late! They are currently at {curr_full_station}."

                    if train_data_root == "48":
                        on_time = 45
                        late = 46
                        horribly_late = 90
                        insanely_late = 120

                        if curr_status == "enroute":
                            if curr_delay <= on_time:
                                State.data = f"Teebs and Chance are on time! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= late:
                                State.data = f"Teebs and Chance are running late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                State.data = f"Teebs and Chance are horribly late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                State.data = f"Teebs and Chance are insanely late! They are currently {curr_status} to {curr_full_station}."

                        if curr_status == "station":
                            if curr_delay <= on_time:
                                State.data = f"Teebs and Chance are on time! They are currently at {curr_full_station}."
                            elif curr_delay <= late:
                                State.data = f"Teebs and Chance are running late! They are currently at {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                State.data = f"Teebs and Chance are horribly late! They are currently at {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                State.data = f"Teebs and Chance are insanely late! They are currently at {curr_full_station}."

                    if train_data_root == "89":
                        on_time = 45
                        late = 46
                        horribly_late = 90
                        insanely_late = 120

                        if curr_status == "enroute":
                            if curr_delay <= on_time:
                                self.data = f"Teebs and Chance are on time! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= late:
                                self.data = f"Teebs and Chance are running late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                self.data = f"Teebs and Chance are horribly late! They are currently {curr_status} to {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                self.data = f"Teebs and Chance are insanely late! They are currently {curr_status} to {curr_full_station}."

                        if curr_status == "station":
                            if curr_delay <= on_time:
                                self.data = f"Teebs and Chance are on time! They are currently at {curr_full_station}."
                            elif curr_delay <= late:
                                self.data = f"Teebs and Chance are running late! They are currently at {curr_full_station}."
                            elif curr_delay <= horribly_late:
                                self.data = f"Teebs and Chance are horribly late! They are currently at {curr_full_station}."
                            elif curr_delay >= insanely_late:
                                self.data = f"Teebs and Chance are insanely late! They are currently at {curr_full_station}."
        else:
            self.data = "Unable to retrieve train status. Please check back later."


@rx.page(on_load=State.get_train_status, title="Teebs and Chance's Adventure")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.flex(
                rx.heading("Welcome to Teebs and Chance's Amazing Adventure!", size="9"),
                rx.image(src='/heads.png'),
                align="center",
                justify="center",
                width="100%",
                direction="column",
            ),
            rx.divider(),
            rx.flex(
                rx.text(State.data, size="9"),
                align="center",
                justify="center",
            ),
        ),
    )


app = rx.App()
