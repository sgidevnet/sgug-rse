%global srcname http-client
%global desc Quickly and easily access any RESTful or RESTful-like API.

Name:           python-%{srcname}
Version:        3.2.7
Release:        2%{?dist}
Summary:        HTTP REST client, simplified for Python
License:        MIT
URL:            https://github.com/sendgrid/%{name}
Source0:        %{url}/archive/%{version}.tar.gz

BuildArch:      noarch


%description
%{desc}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}
This is a Python 3 version of the package.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


%check
py.test-3 -v


%files -n python3-%{srcname}
%license LICENSE.md
%doc README.rst CHANGELOG.md USAGE.md
%{python3_sitelib}/python_http_client/
%{python3_sitelib}/python_http_client-%{version}-py%{python3_version}.egg-info/
%exclude %{python3_sitelib}/tests


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.7-2
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.7-1
- Update to 3.2.7 (#1819947)

* Thu Mar 05 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.6-1
- Update to 3.2.6 (#1805003)

* Thu Feb 20 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.5-1
- Update to 3.2.5 (#1805003)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.4-1
- New upstream version 3.2.4 (bz#1794624)

* Thu Jan 23 2020 Lumír Balhar <lbalhar@redhat.com> - 3.2.3-1
- New upstream version 3.2.3 (bz#1794323)

* Fri Sep 13 2019 Lumír Balhar <lbalhar@redhat.com> - 3.2.1-1
- New upstream version 3.2.1 (bz#1751784)

* Thu Sep 12 2019 Lumír Balhar <lbalhar@redhat.com> - 3.2.0-1
- New upstream version 3.2.0 (bz#1751451)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Lumír Balhar <lbalhar@redhat.com> - 3.1.0-6
- Skip useles failing test

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Lumír Balhar <lbalhar@redhat.com> - 3.1.0-4
- Get rid of Python 2 subpackage
- Resolves: rhbz#1639322

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Lumír Balhar <lbalhar@redhat.com> - 3.1.0-1
- New usptream version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 16 2017 Lumír Balhar <lbalhar@redhat.com> 3.0.0-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-2
- Rebuild for Python 3.6

* Thu Aug 11 2016 Dominika Krejci <dkrejci@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Mon Jul 18 2016 Dominika Krejci <dkrejci@redhat.com> - 2.1.1-1
- Initial release

