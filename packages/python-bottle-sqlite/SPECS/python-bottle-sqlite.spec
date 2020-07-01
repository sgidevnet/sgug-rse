%global srcname bottle-sqlite
Name:           python-%{srcname}
Version:        0.1.3
Release:        14%{?dist}
Summary:        SQLite3 integration for Bottle WSGI framework

License:        MIT
URL:            http://bottlepy.org
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Bottle-sqlite is a plugin that integrates SQLite3 with your Bottle application.
It automatically connects to a database at the beginning of a request, passes
the database handle to the route callback and closes the connection afterwards.

To automatically detect routes that need a database connection, the plugin
searches for route callbacks that require a db keyword argument (configurable)
and skips routes that do not. This removes any overhead for routes that don't
need a database connection.

%package -n python3-%{srcname}
Summary: SQLite3 integration for Bottle WSGI framework

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-bottle

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Bottle-sqlite is a plugin that integrates SQLite3 with your Bottle application.
It automatically connects to a database at the beginning of a request, passes
the database handle to the route callback and closes the connection afterwards.

To automatically detect routes that need a database connection, the plugin
searches for route callbacks that require a db keyword argument (configurable)
and skips routes that do not. This removes any overhead for routes that don't
need a database connection.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc PKG-INFO
%{python3_sitelib}/bottle_sqlite.py*
%{python3_sitelib}/__pycache__/bottle_sqlite*
%{python3_sitelib}/bottle_sqlite*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.3-8
- Subpackage python2-bottle-sqlite has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.3-2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.1.3-1
- Update to 0.1.3
- Modernize SPEC
- Provide python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 18 2011 Rahul Sundaram <sundaram@fedoraproject.org> - 0.1-1
- Initial spec
