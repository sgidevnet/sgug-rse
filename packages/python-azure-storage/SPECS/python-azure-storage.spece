%global srcname azure-storage
%global common_description This project provides a client library in Python that makes it easy to consume\
Microsoft Azure Storage services.

%global _with_tests 1
%global _with_doc 1

%global azure_sdk_min_version 4.0.0

Name:           python-%{srcname}
Version:        2.1.0
Release:        4%{?dist}
Summary:        Microsoft Azure Storage Library for Python

License:        MIT
URL:            https://github.com/Azure/azure-storage-python/
Source0:        %{url}/archive/v%{version}-file/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?_with_tests}
BuildRequires:  python3-azure-sdk >= %{azure_sdk_min_version}
BuildRequires:  python3-cryptography
BuildRequires:  python3-dateutil
BuildRequires:  python3-requests
BuildRequires:  python3-vcrpy
%endif
%if 0%{?_with_doc}
BuildRequires:  python3-azure-sdk >= %{azure_sdk_min_version}
BuildRequires:  python3-cryptography
BuildRequires:  python3-dateutil
BuildRequires:  python3-pip
BuildRequires:  python3-requests
BuildRequires:  python3-sphinx
%endif
BuildArch:      noarch

%description
%{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{common_description}


%if 0%{?_with_doc}
%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This package provides documentation for %{name}.
%endif


%prep
%autosetup -p0 -n azure-storage-python-%{version}%{?prerelease}-file


%build
for package in azure-storage-nspkg azure-storage-common azure-storage-blob azure-storage-file azure-storage-queue; do
    pushd $package
    %py3_build
    popd
done

%if 0%{?_with_doc}
%make_build -C doc/ html SPHINXBUILD=sphinx-build-3
rm doc/_build/html/.buildinfo
%endif


%install
for package in azure-storage-nspkg azure-storage-common azure-storage-blob azure-storage-file azure-storage-queue; do
    pushd $package
    %py3_install
    popd
done


%check
%if 0%{_with_tests}
PYTHONPATH=
for d in azure-*/; do
    PYTHONPATH+="$d:"
done
export PYTHONPATH=${PYTHONPATH%:}
%{__python3} -m unittest discover
%endif


%files -n python3-%{srcname}
%doc BreakingChanges.md ChangeLog.md README.rst
%license LICENSE.txt
%{python3_sitelib}/*


%if 0%{?_with_docs}
%files doc
%doc doc/_build/html/
%license LICENSE.txt
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- Spec cleanp

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.1-2
- Improve unit test checks
- Fix license tag
- Build documentation with Python 3 on Fedora

* Mon Aug 06 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1
