%global srcname stdnum

Name:           python-%{srcname}
Version:        1.13
Release:        2%{?dist}
Summary:        Python module to handle standardized numbers and codes

License:        LGPLv2+
URL:            http://arthurdejong.org/python-stdnum/
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# needed for tests
BuildRequires:  python3-nose


%description
Parse, validate and reformat standard numbers and codes. This library offers
functions for parsing, validating and reformatting standard numbers and codes
in various formats like personal IDs, VAT numbers, IBAN and more.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Parse, validate and reformat standard numbers and codes. This library offers
functions for parsing, validating and reformatting standard numbers and codes
in various formats like personal IDs, VAT numbers, IBAN and more.


%prep
%setup -q
# Remove bundled egg-info
rm -rf %{name}.egg-info


%build
%py3_build


%install
%py3_install


%check
LANG=C.utf-8 nosetests-%{python3_version} -v


%files -n python3-%{srcname}
%license COPYING
%doc NEWS README
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/python_%{srcname}-%{version}-py?.?.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.13-2
- Rebuilt for Python 3.9

* Fri Feb 21 2020 Dan Horák <dan[at]danny.cz> - 1.13-1
- updated to 1.13 (#1792735)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Dan Horák <dan[at]danny.cz> - 1.12-1
- updated to 1.12 (#1765966)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.11-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Dan Horák <dan[at]danny.cz> - 1.11-1
- updated to 1.11 (#1697435)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Dan Horák <dan[at]danny.cz> - 1.3-10
- drop Python2 subpackage (#1627313)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Dan Horák <dan@danny.cz> - 1.3-2
- address comments from package review (#1357566)

* Mon Jul 18 2016 Dan Horák <dan@danny.cz> - 1.3-1
- Initial package.
