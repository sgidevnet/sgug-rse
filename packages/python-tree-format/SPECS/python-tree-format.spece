%global pkgname tree-format
%global commit 4c6de1074d96129b7e03eecdf42fac2cde3b5151
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pkgname}
Version:        0.1.2
Release:        10%{?dist}
Summary:        Python library to generate nicely formatted trees, like the UNIX tree command
License:        ASL 2.0
URL:            https://github.com/jml/tree-format
Source0:        https://github.com/jml/%{pkgname}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         version.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-testtools

%description
Python library to generate nicely formatted trees, like the UNIX `tree` command

%package     -n python3-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkgname}}
%description -n python3-%{pkgname}
Python library to generate nicely formatted trees, like the UNIX `tree` command

%prep
%autosetup -n %{pkgname}-%{commit}

%build
%{py3_build}

%install
%{py3_install}

%check
%{__python3} setup.py test

%files -n python3-%{pkgname}
%license LICENSE
# TODO this is listed as 0.1.0, but our %%{version} is 0.1.2 :(
%{python3_sitelib}/tree_format-0.1.2-py%{python3_version}.egg-info/
%{python3_sitelib}/tree_format/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.1.2-8
- Fixing the package version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-4
- Subpackage python2-tree-format has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.7

* Thu Mar  1 2018 Brett Lentz <brett.lentz@gmail.com> - 0.1.2-1
- initial package
