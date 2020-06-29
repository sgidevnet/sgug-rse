%{?python_enable_dependency_generator}
%global pkg_name flask-babelex
%global mod_name Flask-BabelEx

Name:       python-%{pkg_name}
Version:    0.9.4
Release:    2%{?dist}
Summary:    Adds i18n/l10n support to Flask applications
License:    BSD
URL:        http://github.com/mrjoes/%{pkg_name}
Source0:    https://files.pythonhosted.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildArch:  noarch

%description
Adds i18n/l10n support to Flask applications with the help of the Babel library.

This is fork of official Flask-Babel extension with following features:

1 -  It is possible to use multiple language catalogs in one Flask application;
2 -  Your extension can package localization file(s) and use them if necessary;
3 -  Does not reload localizations for each request.


%package -n python3-%{pkg_name}
Summary:    Adds i18n/l10n support to Flask applications
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Adds i18n/l10n support to Flask applications with the help of the Babel library.

This is fork of official Flask-Babel extension with following features:

1 -  It is possible to use multiple language catalogs in one Flask application;
2 -  Your extension can package localization file(s) and use them if necessary;
3 -  Does not reload localizations for each request.



%prep
%setup -q -n %{pkg_name}-%{version}

%build
%py3_build


%install
%py3_install


%files -n python3-%{pkg_name}
%doc README
%license LICENSE
%{python3_sitelib}/flask_babelex/
%{python3_sitelib}/Flask_BabelEx*.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.9

* Mon May 11 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.4-1
- 0.9.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.3-5
- Enable python dependency generator

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Subpackage python2-flask-babelex has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-2
- Rebuilt for Python 3.7

* Thu Mar 01 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.9.3-1
- Initial package
