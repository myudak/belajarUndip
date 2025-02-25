Kursus Linux untuk Robotika ini mengajarkan dasar-dasar Linux yang penting bagi pengembang robotika, khususnya yang menggunakan ROS. Berikut rangkuman materi yang dipelajari:

**Unit 1: Pengantar**

* Mengapa Linux penting untuk robotika (dukungan ROS, penggunaan luas, fleksibilitas, keamanan).
* Demo skrip Bash untuk mengontrol robot simulasi BB-8.
* Topik yang dibahas: navigasi filesystem, interaksi filesystem, editor vi, izin file, skrip Bash, manajemen proses, koneksi jarak jauh (ssh).
* Pembelajaran berbasis praktik dengan simulasi robot BB-8.

**Unit 2: Dasar-dasar Linux**

* Navigasi filesystem:
    * `cd`: berpindah direktori.
    * `pwd`: menampilkan direktori saat ini.
    * `ls`: menampilkan isi direktori.
    * `~`: singkatan untuk direktori home.
    * `../`: berpindah ke direktori parent.
* Interaksi filesystem:
    * `mkdir`: membuat direktori baru.
    * `touch`: membuat file baru.
    * `vi`: editor teks untuk memodifikasi file.  Penjelasan mode command dan insert, menyimpan (:wq), keluar (:q), dan memaksa keluar (:q!).
    * `mv`: memindahkan file atau direktori.
    * `cp`: menyalin file (`cp -r` untuk direktori).
    * `rm`: menghapus file (`rm -r` untuk direktori).
* Pengenalan skrip Python untuk kontrol robot dan eksekusi dengan `python` dan `rosrun`.
* Memperbaiki error "permission denied" saat menjalankan skrip.

**Unit 3: Utilitas Lanjutan**

* Izin file (permissions):
    * Tipe izin: read (r), write (w), execute (x).
    * Grup izin: owner, group, others.
    * `chmod`: mengubah izin file (misalnya `chmod +x`, `chmod 755`).
* Skrip Bash:
    * `#!/bin/bash`: shebang untuk menandai skrip Bash.
    * `echo`: menampilkan teks ke terminal.
    * Menerima parameter/argumen ($1, $2, dst).
* File `.bashrc`: skrip yang dijalankan setiap kali sesi Shell baru dimulai.  Digunakan untuk kustomisasi Shell, termasuk pengaturan environment variables.
* Environment Variables:
    * `export`: menampilkan dan mengatur environment variables.
    * `grep`: memfilter output (misalnya `export | grep ROS`).
    * Contoh penggunaan `ROS_PACKAGE_PATH`.

**Unit 4: Utilitas Lanjutan Bagian 2**

* Proses Linux:
    * Foreground dan background processes.
    * `htop`: menampilkan proses secara real-time.
    * `ps faux`: menampilkan informasi proses.
    * `grep`: memfilter proses (misalnya `ps faux | grep nama_proses`).
* Mengakhiri Proses:
    * Ctrl+C: mengirimkan sinyal SIGINT (dapat diintersep program).
    * Ctrl+Z: mengirimkan sinyal SIGTSTOP (menunda proses dan memindahkan ke background).
    * `bg`: melanjutkan eksekusi proses background yang ditunda.
    * `kill`: mengakhiri proses berdasarkan PID.  Menjalankan proses di background dengan `&`.
* SSH:
    * `ssh user@host -p port`: terhubung ke mesin jarak jauh.
    * Menjelaskan arsitektur client-server dan penggunaan dalam robotika.
* `apt`, `sudo`:
    * `sudo`: menjalankan perintah sebagai superuser.
    * `apt-get update`: memperbarui database paket.
    * `apt-get install`: menginstal paket.


Intinya, kursus ini mengajarkan perintah dan konsep Linux yang penting untuk berinteraksi dengan sistem Linux, menjalankan program, mengelola file dan direktori, serta terhubung ke mesin jarak jauh. Semua ini difokuskan pada konteks pengembangan robotika, khususnya yang menggunakan ROS.


Linux penting untuk robotika karena beberapa alasan kunci, terutama yang berkaitan dengan dukungan ROS, penggunaan luas di komunitas, fleksibilitas, dan keamanan:

**1. Dukungan ROS (Robot Operating System):**

* **Kompatibilitas Penuh:** ROS didesain dan dikembangkan terutama untuk Linux.  Meskipun ada upaya untuk porting ROS ke sistem operasi lain seperti Windows dan macOS, dukungan dan kompatibilitasnya tidak selengkap di Linux. Banyak paket dan library ROS bergantung pada fitur-fitur spesifik Linux.
* **Stabilitas dan Performa:** Linux menawarkan stabilitas dan performa yang handal untuk menjalankan aplikasi robotika yang kompleks dan intensif sumber daya, terutama yang menggunakan ROS. Kernel Linux yang open-source memungkinkan optimasi dan penyesuaian yang lebih baik untuk kebutuhan spesifik robot.
* **Komunitas dan Ekosistem:**  Sebagian besar komunitas ROS berbasis Linux.  Dokumentasi, tutorial, dan dukungan komunitas ROS terfokus pada Linux.  Ini mempermudah pengembang robotika untuk mendapatkan bantuan, berbagi kode, dan berkolaborasi.

**2. Penggunaan Luas di Komunitas Robotika:**

* **Standar Industri:** Linux telah menjadi standar de facto di industri robotika, baik untuk riset, pengembangan, maupun penerapan di dunia nyata.  Banyak platform robotika populer, seperti robot humanoid, mobile robot, dan manipulator, menggunakan Linux sebagai sistem operasi utama.
* **Akses ke Perangkat Keras:** Linux memiliki dukungan driver yang luas untuk berbagai macam perangkat keras robotika, seperti sensor, aktuator, dan kontroler.  Ini menyederhanakan proses integrasi perangkat keras dengan sistem robot.
* **Open-Source dan Gratis:** Sifat open-source Linux membuatnya mudah diakses dan dimodifikasi oleh pengembang robotika.  Ini memungkinkan fleksibilitas dan kustomisasi yang tinggi, serta mengurangi biaya lisensi perangkat lunak.

**3. Fleksibilitas dan Kustomisasi:**

* **Kernel yang Dapat Dikonfigurasi:** Kernel Linux dapat dikonfigurasi dan dioptimasi untuk kebutuhan spesifik robot, seperti real-time performance dan akses langsung ke perangkat keras.
* **Beragam Distribusi:** Tersedia berbagai macam distribusi Linux yang dapat dipilih sesuai dengan kebutuhan robot, mulai dari distribusi yang ringan dan embedded hingga distribusi yang lengkap dan kaya fitur.
* **Akses ke Source Code:**  Karena open-source, pengembang dapat memodifikasi source code Linux untuk memenuhi kebutuhan khusus robot atau mengintegrasikan fitur-fitur baru.

**4. Keamanan:**

* **Kontrol Akses yang Granular:** Linux menawarkan kontrol akses yang granular untuk file dan direktori, yang penting untuk menjaga keamanan sistem robot.
* **Komunitas Keamanan yang Aktif:** Komunitas open-source Linux yang besar dan aktif terus memantau dan memperbaiki kerentanan keamanan.  Update keamanan tersedia secara teratur.
* **Isolasi Proses:** Linux menyediakan mekanisme isolasi proses yang kuat, yang membantu mencegah malware dan serangan siber menyebar ke seluruh sistem robot.

Dengan semua keuntungan ini, Linux menjadi pilihan yang ideal untuk pengembangan dan penerapan sistem robotika, terutama yang menggunakan ROS.  Kemampuannya untuk beradaptasi dengan berbagai kebutuhan, dukungan komunitas yang kuat, dan fokus pada keamanan menjadikannya platform yang handal dan efisien untuk inovasi di bidang robotika.

ROS 2 (Robot Operating System 2) builds upon the foundation of ROS 1 with a focus on improved performance, reliability, and support for real-time systems and embedded platforms.  Here's a summary of key ROS 2 programming concepts and command-line tools:

**Key ROS 2 Concepts:**

* **Nodes:**  Fundamental building blocks of a ROS 2 system.  Nodes encapsulate computation and communication.
* **Topics:**  Named buses used for asynchronous, many-to-many communication between nodes.  Publishers publish messages on a topic, and subscribers subscribe to a topic to receive those messages.
* **Services:**  Used for synchronous, request-response communication between nodes.  A client sends a request to a service server, and the server processes the request and returns a response.
* **Actions:**  Similar to services, but allow for goals to be canceled and provide feedback during execution.  Useful for long-running tasks.
* **Parameters:**  Configuration values that can be dynamically set and retrieved by nodes.
* **Quality of Service (QoS):**  Defines how data is delivered over the network, such as reliability, durability, and history.
* **Launch Files:**  XML files used to describe and launch complex ROS 2 systems.

**ROS 2 Command-Line Tools:**

* **`ros2 run <package_name> <executable_name>`:** Launches a ROS 2 node.
* **`ros2 node list`:** Lists running ROS 2 nodes.
* **`ros2 node info <node_name>`:** Displays information about a specific node, such as its publishers, subscribers, services, and actions.
* **`ros2 topic list`:** Lists available topics.
* **`ros2 topic echo <topic_name>`:** Prints messages published on a topic to the console.
* **`ros2 topic info <topic_name>`:** Displays information about a topic, such as its type and publishers/subscribers.
* **`ros2 topic pub <topic_name> <message_type> <message_data>`:** Publishes a message to a topic.
* **`ros2 service list`:** Lists available services.
* **`ros2 service call <service_name> <service_type> <request_data>`:** Calls a service.
* **`ros2 service info <service_name>`:** Displays information about a service.
* **`ros2 action list`:** Lists available actions.
* **`ros2 action send_goal <action_name> <action_type> <goal_data>`:** Sends a goal to an action server.
* **`ros2 action info <action_name>`:** Displays information about an action.
* **`ros2 param list`:** Lists parameters of a node.
* **`ros2 param get <node_name> <parameter_name>`:** Gets the value of a parameter.
* **`ros2 param set <node_name> <parameter_name> <value>`:** Sets the value of a parameter.
* **`ros2 param dump <node_name>`:** Dumps all parameters of a node to a YAML file.
* **`ros2 launch <package_name> <launch_file_name>`:** Launches a ROS 2 system described in a launch file.

**ROS 2 Programming (C++ Example):**

```cpp
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  auto node = rclcpp::Node::make_shared("my_node");
  auto publisher = node->create_publisher<std_msgs::msg::String>("my_topic", 10);
  auto message = std_msgs::msg::String