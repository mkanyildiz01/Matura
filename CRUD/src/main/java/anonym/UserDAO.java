package anonym;
/**
 * Autor: Kanyildiz Muhammedhizir
 * Klasse: 4AHITM
 * Datum: 06.10.2016
*/

import java.util.List;

import org.hibernate.Criteria;
import org.hibernate.Query;
import org.hibernate.Session;

/**
 * Die UserDAO Klasse dient zur Verbindung und für den Trasfer von Daten.
 * Im Hintergrund verwendet wird Hibernate benützt.
 * 
 */
public class UserDAO {
	
	/**
	 * saves a user into the db (self-explaining)
	 */
	public void save(User user) {
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		session.save(user);
		session.getTransaction().commit();
		session.close();
	}
	/**
	 * determines a new id
	 */
	public void delete(User user) {
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		session.delete(user);
		session.getTransaction().commit();
		session.close();
	}
	/**
	 * opens a new session and reads users that matches the Critera (obviously every user (User.class))
	 */
	public void update(User user) {
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		session.update(user);
		session.getTransaction().commit();
		session.close();
	}
	/**
	 * deletes a user
	 */
	public List<User> read() {
		Session session = HibernateUtil.getSessionFactory().openSession();
		session.beginTransaction();
		Criteria cr = session.createCriteria(User.class);
		List<User> tmp = cr.list();
		session.getTransaction().commit();
		session.close();
		return tmp;
	}
	/**
	 * updates a user
	 */
	public Integer getId() {
		Session session = HibernateUtil.getSessionFactory().openSession();
		String hql = "select max(user.id) from User user";
		Query query = session.createQuery(hql);
		List<Integer> results = query.list();
		Integer userId = 1;
		if (results.get(0) != null) {
			userId = results.get(0) + 1;
		}
		session.close();
		return userId;
	}
}