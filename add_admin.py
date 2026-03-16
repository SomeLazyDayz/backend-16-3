from app import app, db, User

with app.app_context():
    admin = User.query.filter_by(role='admin').first()
    if not admin:
        admin = User(
            name='Admin', 
            email='admin@giotam.com', 
            phone='0123456789', 
            password='admin', 
            role='admin', 
            address='BV Chợ Rẫy'
        )
        db.session.add(admin)
        db.session.commit()
        print('✅ Đã tạo tài khoản admin thành công!')
    else:
        print('⚠️ Tài khoản admin đã tồn tại.')