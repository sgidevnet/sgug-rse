%{?python_enable_dependency_generator}
%global pkgname jinja2-time

Name:           python-jinja2-time
Version:        0.2.0
Release:        12%{?dist}
Summary:        Jinja2 Extension for Dates and Times

License:        MIT
URL:            https://github.com/hackebrot/jinja2-time
Source0:        https://github.com/hackebrot/%{pkgname}/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Jinja2 Extension for Dates and Times

%package     -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-devel
BuildRequires:  python3-arrow
BuildRequires:  python3-jinja2

%description -n python3-%{pkgname}
Jinja2 Extension for Dates and Times.


%prep
%autosetup -n %{pkgname}-%{version}

%build

%{py3_build}

%install

%{py3_install}

%check

%{__python3} setup.py test


%files -n python3-%{pkgname}
%license LICENSE
%doc *.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-6
- Enable python dependency generator

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Subpackage python2-jinja2-time has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.7

* Tue Apr 3 2018 Brett Lentz <brett.lentz@gmail.com> - 0.2.0-2
- fix deps

* Wed Mar 7 2018 Brett Lentz <brett.lentz@gmail.com> - 0.2.0-1
- initial packaging
