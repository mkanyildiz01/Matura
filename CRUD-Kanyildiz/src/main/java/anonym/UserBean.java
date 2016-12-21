package anonym;
/**
 * Autor: Kanyildiz Muhammedhizir
 * Klasse: 4AHITM
 * Datum: 06.10.2016
*/

import java.util.List;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;

/**
 * Managedbean fuer die JSF Seiten. 
 * Ruft immer die entsprechenden Methoden auf um die CRUD auszufuehren. 
 * Alle Attribute entsprechende Getter und Setter Methoden haben, damit die Bean zugreifen kann. 
 */

@ManagedBean(name = "userBean", eager = true)
@RequestScoped
public class UserBean {
	private String vorname;
	private String nachname;
	private Integer age;
	private List<User> users;
	private Integer select; 
	public UserBean() {
		readUser();
	}
	/**
	 * creates and saves a new user
	 * @return Outputfile
	 */
	public String saveUser() {
		UserDAO userDao = new UserDAO();
		Integer userId = userDao.getId();
		User user = new User(userId, vorname, nachname, age);
		userDao.save(user);
		System.out.println("User successfully saved.");
		return "Output";
	}
	/**
	 * deletes a list of users
	 * @return Outputfile
	 */
	public String deleteUser() {
		UserDAO userDao = new UserDAO();
		Integer userId = select;
		User user = new User(userId, vorname, nachname, age);
		userDao.delete(user);
		System.out.println("User successfully deleted.");
		return "Output";
	}
	/**
	 * updates a user
	 * if no user is selected or if a attribute is not chanced, it doesnt get changed
	 * @return Outputfile
	 */
	public String updateUser() {
		UserDAO userDao = new UserDAO();
		Integer userId = select;
		User user = new User(userId, vorname, nachname, age);
		userDao.update(user);
		System.out.println("User successfully updated.");
		return "Output";
	}
	public String readUser() {
		UserDAO userDao = new UserDAO();
		users = userDao.read();
		return "read";
	}

	public String getVorname() {
		return vorname;
	}

	public void setVorname(String vorname) {
		this.vorname = vorname;
	}

	public String getNachname() {
		return nachname;
	}

	public void setNachname(String nachname) {
		this.nachname = nachname;
	}

	public Integer getAge() {
		return age;
	}

	public void setAge(Integer age) {
		this.age = age;
	}

	public List<User> getUsers() {
		return users;
	}

	public void setUsers(List<User> users) {
		this.users = users;
	}

	public Integer getSelect() {
		return select;
	}

	public void setSelect(Integer select) {
		this.select = select;
	}

}