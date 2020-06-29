%global srcname pysword
%global commit 9a15ab595f24f934c4871e5989b3769ed8d4f9c2
%global sum Open source python API wrapper for Sword Bible files
%global desc %{expand: A native Python reader of the SWORD Project Bible Modules.
Reads SWORD bible files (not commentaries etc.)
Detection of locally installed Swrod bible modules.
Supports all known SWORD module formats (ztext, ztext4, rawtext, rawtext4)
Read from zipped modules, like those available from
http://www.crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles
Cleans the extracted text of OSIS, GBF or ThML tags. 
Supports both python 2 and 3 (tested with 2.7 and 3.5) }

Summary: %{sum}
Name: python-%{srcname}
Version: 0.2.7
Release: 2%{?dist}
Source0: https://gitlab.com/tgc-dk/%{srcname}/repository/archive.tar.gz?ref=%{version}#/%{srcname}-%{version}.tar.gz
Source1: testdata-0.2.7.tar.gz
License: GPLv2
BuildArch: noarch

URL: https://gitlab.com/tgc-dk/pysword

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}-%{commit}
%autosetup -N -T -D -a 1 -n %{srcname}-%{version}-%{commit}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Tim Bentley <Tim.Bentley@openlp.org>  - 0.2.7-0
- Upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-7
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Tim Bentley <Tim.Bentley@openlp.org>  - 0.2.6-0
- Upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-3
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.5-2
- 0.2.5 Release repackage

* Fri Mar 23 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.5-1
- 0.2.5 Release repackage

* Sat Mar 17 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.4-1
- 0.2.4 Release repackage

* Sun Feb 11 2018 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.3-1
- 0.2.3 Release repackage

* Sat Nov 26 2016 Tim Bentley <Tim.Bentley@openlp.org> - 0.2.3-0
- 0.2.3 Release   
