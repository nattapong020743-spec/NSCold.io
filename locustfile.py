from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # หน่วงเวลาสุ่มระหว่าง 1 ถึง 3 วินาทีก่อนกดคลิกหน้าต่อไป (จำลองคนใช้งานจริง)
    wait_time = between(1, 3)

    @task
    def index_page(class_instance):
        # ทดสอบเข้าหน้าแรกของเว็บไซต์
        class_instance.client.get("/")

    @task(2) # ให้ความสำคัญ/เข้าชมหน้านี้บ่อยเป็น 2 เท่า
    def about_page(class_instance):
        # เปลี่ยนเป็นเส้นทาง (Route) หน้าบริการหรือหน้าเกี่ยวกับบริษัท เช่น /services หรือ /about
        class_instance.client.get("/services")