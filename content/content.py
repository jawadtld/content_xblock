"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String, Integer
from xblock.fragment import Fragment


class ContentXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    display_name = String(
        display_name="Display Name",
        help="Display name of the component",
        default="Content template",
        scope=Scope.content)

    subtopic = String(
        default="subtopic",
        scope=Scope.content,
        help="Name of subtopic")

    subtopic_desc = String(
        default="subtopic description",
        scope=Scope.content,
        help="Subtopic description")

    image_url = String(
        default="http://docs.edx.org/edx-docs/assets/images/logo-edx.png",
        scope=Scope.content,
        help="Enter url for the image, which will be displayed below the subtopic description")

    image_desc = String(
        default="Image description",
        scope=Scope.content,
        help="Description for the image")

    sim_url = String(
        default="https://phet.colorado.edu/sims/html/states-of-matter/latest/states-of-matter_en.html",
        scope=Scope.content,
        help="Enter simulation URL")

    sim_desc = String(
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help="Small description about the simulation")

    anim_url = String(
        default="https://www.youtube.com/embed/Fd9a24c1iy4",
        scope=Scope.content,
        help="Enter animation URL")

    anim_desc = String(
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help="Small description about the animation")

    vid_url = String(
        default="https://www.youtube.com/embed/J_EyP1SAfUo",
        scope=Scope.content,
        help="Enter video URL")

    vid_desc = String(
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help="Small description about the video")

    game_url = String(
        default="http://54.70.206.130/WebGL_Builds/Bowling_WGL/",
        scope=Scope.content,
        help="Enter game URL")

    game_desc = String(
        default="At least two objects must interact for a force to play a role. Interaction between the objects can be physical or non-physical.",
        scope=Scope.content,
        help="Small description about the game")

    page_views = Integer(
        default=0,
        scope=Scope.user_state_summary,
        help="Small description about the game")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ContentXBlock, shown to students
        when viewing courses.
        """
        self.page_views += 1
        html = self.resource_string("static/html/content.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/content.css"))
        js = self.resource_string("static/js/src/content.js")
        frag.add_javascript(js)
        frag.initialize_js('ContentXBlock')
        return frag

    def studio_view(self, context):
        """
        The primary view of the ContentXBlock, shown to studio view.
        """
        html = self.resource_string("static/html/content_edit.html")
        frag = Fragment(html.format(display_name=self.display_name,subtopic=self.subtopic,subtopic_desc=self.subtopic_desc,image_url=self.image_url,image_desc=self.image_desc,sim_url=self.sim_url,sim_desc=self.sim_desc,anim_url=self.anim_url,anim_desc=self.anim_desc,vid_url=self.vid_url,vid_desc=self.vid_desc,game_url=self.game_url,game_desc=self.game_desc,page_views=self.page_views))
        frag.add_css(self.resource_string("static/css/content.css"))
        js = self.resource_string("static/js/src/content_edit.js")
        frag.add_javascript(js)
        frag.initialize_js('ContentXBlockEditor')
        return frag


    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """
        Called when submitting the form in Studio.
        """
        self.display_name = data.get('display_name')
        self.subtopic = data.get('subtopic')
        self.subtopic_desc = data.get('subtopic_desc')
        self.image_url = data.get('image_url')
        self.image_desc = data.get('image_desc')
        self.sim_url = data.get('sim_url')
        self.sim_desc = data.get('sim_desc')
        self.anim_url = data.get('anim_url')
        self.anim_desc = data.get('anim_desc')
        self.vid_url = data.get('vid_url')
        self.vid_desc = data.get('vid_desc')
        self.game_url = data.get('game_url')
        self.game_desc = data.get('game_desc')
        return {'result': 'success'}


    @XBlock.json_handler
    def fieldstojs(self, data, suffix=''):
        """
        Used to pass values of fields to content.js
        """
        return {'sim_url':self.sim_url,'anim_url':self.anim_url,'vid_url':self.vid_url,'game_url':self.game_url,'result':'success'}


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ContentXBlock",
             """<content/>
             """),
            ("Multiple ContentXBlock",
             """<vertical_demo>
                <content/>
                <content/>
                <content/>
                </vertical_demo>
             """),
        ]
