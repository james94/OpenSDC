variable "TAG" {
    default = "latest"
}

group "default" {
    targets = [
        "s_apt",
        "s_ros_humble",
        "sdvcore"
    ]
    network = "host"
    platforms = ["linux/amd64"]
}

target "s_apt" {
    context = "./s_10_apt"
    tags = ["s_apt:${TAG}"]
    output = ["type=docker"]
}

target "s_ros_humble" {
    context = "./s_20_ros_humble"
    contexts = {
        s_apt = "target:s_apt"
    }
    tags = ["s_ros_humble:${TAG}"]
    output = ["type=docker"]
}

target "sdvcore" {
    context = "./s_30_entry"
    contexts = {
        s_ros_humble = "target:s_ros_humble"
        s_apt = "target:s_apt"
    }
    tags = ["sdvcore:${TAG}"]
    output = ["type=docker"]
}
