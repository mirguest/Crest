package hep.crest.data.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;


@Component
@ConfigurationProperties("crest")
public class CrestProperties {

	
	private String dump_dir;
	private String schemaname;
	private String security;
	private String synchro;
	private String webstaticdir;
	private String authenticationtype;

	public String getDump_dir() {
		System.out.println("property dump_dir has value: "+dump_dir);
		return dump_dir;
	}

	public void setDump_dir(String dump_dir) {
		this.dump_dir = dump_dir;
	}

	public String getSchemaname() {
		System.out.println("property schemaname has value: "+schemaname);
		return schemaname;
	}

	public void setSchemaname(String schemaname) {
		this.schemaname = schemaname;
	}

	public String getSecurity() {
		return security;
	}

	public void setSecurity(String security) {
		this.security = security;
	}

	public String getSynchro() {
		return synchro;
	}

	public void setSynchro(String synchro) {
		this.synchro = synchro;
	}

	public String getWebstaticdir() {
		return webstaticdir;
	}

	public void setWebstaticdir(String webstaticdir) {
		this.webstaticdir = webstaticdir;
	}

	public String getAuthenticationtype() {
		return this.authenticationtype;
	}
	
	public void setAuthenticationtype(String authtype) {
		this.authenticationtype = authtype;
	}
	
}
