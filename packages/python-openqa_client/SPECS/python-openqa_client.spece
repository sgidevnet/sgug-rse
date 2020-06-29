%global sum     Python client library for openQA API
%global desc    The openqa_client Python library provides convenient access to the \
openQA web API, using the requests HTTP request library.

%global srcname         openqa_client

%global github_owner    os-autoinst
%global github_name     openQA-python-client
%global github_version  4.1.0
# if set, will be a post-release snapshot build, otherwise a 'normal' build
#global github_commit   080d03858b7b12f144770af8ceb938fe6c7dbb11
#global github_date     20170130
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

Name:           python-openqa_client
Version:        %{github_version}
Release:        2%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        %{sum}

License:        GPLv2+
URL:            https://github.com/%{github_owner}/%{github_name}/
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-openqa_client
Summary:        %{sum}
BuildRequires:  pyproject-rpm-macros

%{?python_provide:%python_provide python3-openqa_client}
Obsoletes:      python2-openqa_client < %{version}-%{release}

%description -n python3-openqa_client
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# setuptools-git is needed to build the source distribution, but not
# for packaging, which *starts* from the source distribution
sed -i -e 's., "setuptools-git"..g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox


%files -n python3-openqa_client
%doc README.md CHANGELOG.md
%license COPYING
%{python3_sitelib}/openqa_client*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.9

* Fri Mar 13 2020 Adam Williamson <awilliam@redhat.com> - 4.1.0-1
- New release 4.1.0 (handle YAML responses from API)

* Fri Feb 28 2020 Adam Williamson <awilliam@redhat.com> - 4.0.0-1
- New release 4.0.0 (modernization release, no functional changes)

* Thu Feb 27 2020 Adam Williamson <awilliam@redhat.com> - 3.0.4-1
- New release 3.0.4
- Run tests in %check (now there are some)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Adam Williamson <awilliam@redhat.com> - 2.0.0-1
- Update to new release 2.0.0 (JOB_INCOMPLETE_RESULTS removed)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Adam Williamson <awilliam@redhat.com> - 1.3.2-1
- New release 1.3.2 (updated constants for upstream changes)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Adam Williamson <awilliam@redhat.com> - 1.3.1-5
- Disable Python 2 build on F30+ / RHEL 8+

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Adam Williamson <awilliam@redhat.com> - 1.3.1-1
- New release 1.3.1 (updated constants for upstream changes)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Adam Williamson <awilliam@redhat.com> - 1.3.0-1
- Initial package
