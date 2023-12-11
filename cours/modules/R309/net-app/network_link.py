from typing import (Union, Callable)
from coords import Coords
from tkinter import Canvas
from os import get_terminal_size

class NetworkLink:
    def __init__(self, x: int, y: int, canvas: Canvas, equipment_tag: int, fragmented: bool = False):
        self.start_coords = Coords(x, y)
        self.end_coords = None
        self.tag = None
        self.start_equipment = equipment_tag
        self.end_equipment = None

        self.canvas = canvas
        self.is_fragmented: bool = fragmented
        self.segments = []
        self.reverse_links_dict = None

        self.bindings = {}

        self.term_size_x, self.term_size_y = get_terminal_size()

        self.CTRL_LINK_SPACING = 30

    def setEndCoords(self, x: int, y: int, equipment_tag: int, force: bool = False):
        if not force:
            if self.end_coords is None:
                self.end_coords = Coords(x, y)
                self.end_equipment = equipment_tag
                return True
            else:
                return False
        else:
            self.end_coords = Coords(x, y)
            self.end_equipment = equipment_tag
            return True

    def updateStartCoords(self, x: int, y: int):
        self.start_coords.update(x, y)

    def updateEndCoords(self, x: int, y: int):
        self.end_coords.update(x, y)

    def addBinding(self, event_to_bind: str, non_fragmented_call: Callable, fragmented_call: Callable = None):
        if self.is_fragmented:
            segment_binding = []
            for segment_id in self.segments:
                segment_binding.append({
                    "id": self.canvas.tag_bind(segment_id, event_to_bind, fragmented_call),
                    "non-fragmented-call": non_fragmented_call,
                    "fragmented-call": fragmented_call,
                })
        else:
            segment_binding = [{
                "id": self.canvas.tag_bind(self.tag, event_to_bind, non_fragmented_call),
                "non-fragmented-call": non_fragmented_call,
                "fragmented-call": fragmented_call
            }]

        self.bindings.update({
            event_to_bind: segment_binding
        })

    def removeBinding(self, event_to_unbind: str):
        if self.is_fragmented:
            for i in range(0, len(self.segments)):
                segment_id = self.segments[i]
                segment_binding = self.bindings[event_to_unbind][0]["id"]

                self.canvas.tag_unbind(segment_id, segment_binding)
        else:
            if self.tag is not None:
                self.canvas.tag_unbind(self.tag, self.bindings[event_to_unbind])
            else:
                pass

    def segmented_line(self, x0, y0, x1, y1):

        ### Compute the absolute distance between the origin and the destination
        dx: int = int(abs(x0 - x1))
        dy: int = int(abs(y0 - y1))

        ### Compute the theoric required number of segments from each absolute distance
        ### based on the global constant `CTRL_LINK_SPACING`
        nx = dx // self.CTRL_LINK_SPACING
        ny = dy // self.CTRL_LINK_SPACING

        ### Delta is our decisive number of segments we're gonna create.
        ### We take the longest cut of either `nx` or `ny`.
        ### We then compute the length of the segments.
        delta = nx if nx > ny else ny
        if delta != 0:
            if delta == nx:
                ny = delta
                ny_length = dy // delta
                nx_length = dx // delta
            else:
                nx = delta
                nx_length = dx // delta
                ny_length = dy // delta
        else:
            nx_length = 0
            ny_length = 0

        segments = []

        print(f"\n{self.term_size_x*'-'}\n")

        print(f"DX: {dx}, DY: {dy}, X-Segments: {nx}, Y-Segments: {ny}, X-Segments-Length: {nx_length}, Y-Segments-Length: {ny_length}, Delta: {delta}")

        print(f"\n{self.term_size_x*'-'}\n")

        ### We create the list of the segments with a rotation of x then y
        for i in range(1, nx+1):
            fragmented_segment_on_x = []
            fragmented_segment_on_y = []
            base_x_segment = []
            base_y_segment = []

            ### We're fragmenting the creation of the segments
            ### of X and Y and the corresponding base segments

            if x1 < x0:
                fragmented_segment_on_x = [x0 - nx_length*(i-1), x0 - (nx_length*i)]
                base_x_segment = [x0 - nx_length*(i-1), x0 - nx_length*(i-1)]
                print(f"Turn n°{i}: x: {x0 - nx_length*(i-1)} -> {x0 - (nx_length*i)},", end=" ")
            else:
                fragmented_segment_on_x = [x0 + nx_length*(i-1), x0 + (nx_length*i)]
                base_x_segment = [x0 + nx_length*(i-1), x0 + nx_length*(i-1)]
                print(f"Turn n°{i}: x: {x0 + nx_length*(i-1)} -> {x0 + (nx_length*i)},", end=" ")

            if y1 < y0:
                fragmented_segment_on_y = [y0 - ny_length*(i-1), y0 - (ny_length*i)]
                base_y_segment = [y0 - ny_length*i, y0 - ny_length*i]
                print(f"y: {y0 - (ny_length*(i-1))} -> {y0 - (ny_length*i)}, old_coords: ({x0}/{y0}) -> ({x1}/{y1})")
            else:
                fragmented_segment_on_y = [y0 + ny_length*(i-1), y0 + (ny_length*i)]
                base_y_segment = [y0 + ny_length*i, y0 + ny_length*i]
                print(f"y: {y0 + (ny_length*(i-1))} -> {y0 + (ny_length*i)}, old_coords: ({x0}/{y0}) -> ({x1}/{y1})")

            segments.append(fragmented_segment_on_x + base_y_segment)
            segments.append(base_x_segment + fragmented_segment_on_y)

        return segments

    def draw(self, reverse_links_dict: dict) -> Union[int, list]:
        x0, y0 = self.start_coords
        if self.end_coords is not None:
            x1, y1 = self.end_coords
        else:
            x1, y1 = x0, y0

        if self.is_fragmented:
            ### We have multiple x-only or y-only segments
            ### from the start coordinates to the end coordinates
            for segment in self.segmented_line(x0, y0, x1, y1):
                x0, x1, y0, y1 = segment
                line_id = self.canvas.create_line(x0, y0, x1, y1)
                self.segments.append(line_id)
                self.canvas.tag_lower(line_id)

                for binding_key, binding_values in self.bindings.items():
                    self.canvas.tag_bind(line_id, binding_key, binding_values["fragmented-call"])

                if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                    self.updateReverseLinksDict(line_id)

            to_return: list = self.segments
        else:
            ### We have one direct diagonal link
            self.tag = self.canvas.create_line(x0, y0, x1, y1)
            self.canvas.tag_lower(self.tag)

            for binding_key, binding_values in self.bindings.items():
                self.canvas.tag_bind(self.tag, binding_key, binding_values["non-fragmented-call"])

            if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                self.updateReverseLinksDict(self.tag)

            to_return: int = self.tag

        return to_return

    def update(self, reverse_links_dict: dict) -> Union[int, list]:
        x0, y0 = self.start_coords
        x1, y1 = self.end_coords

        ### First of all, we're going to verify the validity of the links position
        start_pos = self.canvas.coords(self.start_equipment)
        if self.end_equipment is not None:
            end_pos = self.canvas.coords(self.end_equipment)
        else:
            ### Otherwise, pick by default the given coords
            end_pos = (x1, y1)

        ### If the start equipment position is different, update the start coords
        if (x0, y0) != start_pos:
            self.updateStartCoords(start_pos[0], start_pos[1])

        ### If the end equipment is different, update the end coords
        if (x1, y1) != end_pos:
            self.updateEndCoords(end_pos[0], end_pos[1])

        if self.is_fragmented:
            ### Cleaning the self.tag if we're moving from
            ### direct + diagonal link to direct + segmented link
            if self.tag is not None:
                self.cleanDiagonalLinkContent()

            ### Cleaning the self.segments and the current canvas IDs
            ### if we were already segmented
            if self.segments != []:
                self.cleanSegmentedLinkContent()

            ### We are regenerating the segments one by one
            for segment in self.segmented_line(x0, y0, x1, y1):
                x0, x1, y0, y1 = segment

                ### We're creating the line on the canvas then
                ### lowering the tag to not lock user input on the link object
                line_id = self.canvas.create_line(x0, y0, x1, y1)
                self.canvas.tag_lower(line_id)
                ### We're appending the line_id into the self.segments dictionnary
                self.segments.append(line_id)

                ### We're going through every binding element already created
                ### for links to create a homogeneous set of segments
                for binding_key, binding_values in self.bindings.items():
                    self.canvas.tag_bind(line_id, binding_key, binding_values[0]["fragmented-call"])

                if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                    self.updateReverseLinksDict(line_id)

            to_return: list = self.segments

        else:
            ### Well, what a surprise, we were working with a segmented link
            ### Now, we need to clean the old link
            if self.segments != []:
                self.cleanSegmentedLinkContent()

                if self.tag is not None:
                    self.cleanDiagonalLinkContent()

                self.tag = self.canvas.create_line(x0, y0, x1, y1)
                self.canvas.tag_lower(self.tag)

                for binding_key, binding_values in self.bindings.items():
                    self.canvas.tag_bind(self.tag, binding_key, binding_values[0]["non-fragmented-call"])

                if self.setOrUpdateReverseLinksDict(reverse_links_dict):
                    self.updateReverseLinksDict(self.tag)

            elif self.tag is not None:
                ### In fact, we were already a diagonal link
                self.canvas.coords(self.tag, x0, y0, x1, y1)

            to_return: int = self.tag


        return to_return

    def updateFragmentationStatus(self, fragmentation_value: bool):
        self.is_fragmented = fragmentation_value

    def cleanDiagonalLinkContent(self) -> None:
        """A simple utility to clean the content of a diagonal link.

                CAUTION: The link should be verified before calling this function with:

                    ```py
                    if self.tag is not None:
                        self.cleanDiagonalLinkContent()
                    ```
        """
        self.canvas.delete(self.tag)
        self.deleteFromReverseLinksDict(self.tag)
        self.tag = None

    def cleanSegmentedLinkContent(self) -> None:
        """A simple utility to clean the content of a segmented link.
        """
        ### Firstly, we're unbinding all events from every element
        for event in self.bindings.keys():
            self.removeBinding(event)

        for segment_id in self.segments:
            self.canvas.delete(segment_id)

            ### We're cleaning the current (internal & external) list of segments
            ### Otherwise, we're risking load latency because of the size of the list
            self.segments.pop(self.segments.index(segment_id))
            self.deleteFromReverseLinksDict(segment_id)

    def setOrUpdateReverseLinksDict(self, reverse_dict: dict) -> bool:
        if self.reverse_links_dict is not None:
            if self.reverse_links_dict is not reverse_dict:
                self.reverse_links_dict = reverse_dict
        else:
            self.reverse_links_dict = reverse_dict

        return True

    def updateReverseLinksDict(self, line_id: Union[str, int]) -> None:
        self.reverse_links_dict.update({
            line_id: self
        })

    def deleteFromReverseLinksDict(self, line_id: Union[str, int]) -> None:
        if line_id in self.reverse_links_dict.keys():
            self.reverse_links_dict.pop(line_id)