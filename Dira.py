from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("AWS Architecture", filename="image", outformat="png", show=False):
    EC2("Web Server") >> RDS("Database")>> ELB("Strage")