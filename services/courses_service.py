"""
    # Updated on September 20, 2024, by Neoris
    #
    # Despite this software is developed by Neoris, it belongs to Santillana,
    # either first version of the License, or (at your option) any later version.
    #
"""

from models.responses.get_objects_response import GetObjectsResultResponse
from repositories.database.courses_repository import CoursesRepository


class CourseService(object):
    """
    Class CourseService
    """

    @staticmethod
    def get_courses() -> GetObjectsResultResponse:
        """
        Get Courses
        :Return: CoursesResponse
        """

        courses = CoursesRepository.get_courses()
        return GetObjectsResultResponse.model_validate({"result": {"data": courses}})
