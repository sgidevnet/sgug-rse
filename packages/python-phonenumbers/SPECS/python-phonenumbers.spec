%global pypi_name phonenumbers

%global desc A Python port of libphonenumber, Google's common Java, C++, and\
JavaScript library for parsing, formatting, and validating international phone\
numbers.\


Name:           python-%{pypi_name}
Version:        8.12.5
Release:        1%{?dist}
Summary:        A Python port of Google's libphonenumber

License:        ASL 2.0
URL:            https://github.com/daviddrysdale/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%prep
%autosetup

# Snip the #! from the util.py module
sed -i -e '/^#!\//, 1d' python/%{pypi_name}/util.py


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*.egg-info


%changelog
* Sat Jun 13 2020 Dan Callaghan <djc@djc.id.au> - 8.12.5-1
- new upstream release 8.12.5

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.12.3-2
- Rebuilt for Python 3.9

* Sun May 17 2020 Dan Callaghan <djc@djc.id.au> - 8.12.3-1
- new upstream release 8.12.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Jeremy Cline <jcline@redhat.com> - 8.10.18-8
- Update to v8.10.18

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 8.9.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 8.9.0-4
- Subpackage python2-phonenumbers has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 8.9.0-2
- Rebuilt for Python 3.7

* Fri Feb 23 2018 Jeremy Cline <jeremy@jcline.org> - 8.9.0-1
- Update to latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 8.8.10-1
- Update to latest upstream

* Mon Oct 02 2017 Jeremy Cline <jeremy@jcline.org> - 8.8.2-1
- Update to latest upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jeremy Cline <jeremy@jcline.org> - 8.6.0-1
- Update to the latest upstream release (#1468569)

* Fri Jun 23 2017 Jeremy Cline <jeremy@jcline.org> - 8.5.2-1
- Update to latest upstream

* Wed Jun 21 2017 Jeremy Cline <jeremy@jcline.org> - 8.5.1-2
- Address review comments

* Fri May 19 2017 Jeremy Cline <jeremy@jcline.org> - 8.5.1-1
- Initial package
