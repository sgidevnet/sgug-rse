%{?python_enable_dependency_generator}
%global pkg_name flask-mail
%global mod_name Flask-Mail

Name:       python-%{pkg_name}
Version:    0.9.1
Release:    12%{?dist}
Summary:    Flask extension for sending email
License:    BSD
URL:        http://github.com/mattupstate/%{pkg_name}/
Source0:    https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

%description
A Flask extension for sending email messages.


%package -n python3-%{pkg_name}
Summary:    Flask extension for sending email
BuildRequires:   python3-devel
BuildRequires:   python3-setuptools
BuildRequires:   python3-flask
%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
A Flask extension for sending email messages.


%prep
%setup -q -n %{mod_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/flask_mail.py
%{python3_sitelib}/__pycache__/flask_mail*.py*
%{python3_sitelib}/Flask_Mail*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.1-6
- Enable python dependency generator

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-5
- Subpackage python2-flask-mail has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.1-2
- improve spec file

* Tue Jan  3 2017 Jakub Dorňák <jakub.dornak@misli.cz> - 0.9.1-1
- Initial package
