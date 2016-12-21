package anonym;
/**
 * Autor: Kanyildiz Muhammedhizir
 * Klasse: 4AHITM
 * Datum: 06.10.2016
*/

import org.hibernate.SessionFactory;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;

/**
 * Die HibernateUtil Klasse dient zur Konfiguration von Hibernate. 
 * Sie erzeugt eine Sessionfactory(Verbindungsaufbau).
 */

public class HibernateUtil {
	private static SessionFactory sessionFactory;
	static {
		Configuration configuration = new Configuration().configure("hibernate.cfg.xml");
		StandardServiceRegistryBuilder builder = new StandardServiceRegistryBuilder()
				.applySettings(configuration.getProperties());
		sessionFactory = configuration.buildSessionFactory(builder.build());
	}

	public static SessionFactory getSessionFactory() {
		return sessionFactory;
	}
}