%bcond_without	slang

Summary:	User-friendly text console file manager and visual shell
Name:		mc
Epoch:		1
Version:	4.8.24
Release:	3%{?dist}
License:	GPLv3+
URL:		http://www.midnight-commander.org/
Source0:	http://www.midnight-commander.org/downloads/mc-%{version}.tar.xz
Patch1:		%{name}-spec.syntax.patch
Patch2:		%{name}-rpm.patch
Patch3:		%{name}-python3.patch
Patch4:		%{name}-default_setup.patch
Patch5:		%{name}-tmpdir.patch

Patch100:       mc.sgifixes.patch

#BuildRequires:	e2fsprogs-devel
BuildRequires:  gcc
#BuildRequires:	glib2-devel
#BuildRequires:	gpm-devel
BuildRequires:	groff-base
BuildRequires:	libssh2-devel	>= 1.2.5
BuildRequires:	%{?with_slang:slang-devel}%{!?with_slang:ncurses-devel}
BuildRequires:	pkgconfig
BuildRequires:	perl-generators
Suggests:	mc-python

%description
Midnight Commander is a visual shell much like a file manager, only with
many more features. It is a text mode application, but it also includes
mouse support. Midnight Commander''s best features are its ability to FTP,
view tar and zip files, and to poke into RPMs for specific files.

#%%package python
#Summary:	Midnight Commander s3+ and UC1541 EXTFS backend scripts
#BuildArch:	noarch
#Requires:	%%{name} = %%{epoch}:%%{version}-%%{release}
#Requires:	python3-boto

#%%description python
#Midnight Commander s3+ and UC1541 EXTFS backend scripts.

%prep
%autosetup -p1

# A place to generate the SGUG patch
#exit 1

%build
%configure \
	--enable-charset \
	--enable-largefile \
	--enable-vfs-cpio \
	--enable-vfs-extfs \
	--enable-vfs-fish \
	--enable-vfs-ftp \
	--enable-vfs-sfs \
	--enable-vfs-sftp \
	--enable-vfs-smb \
	--enable-vfs-tar \
	--with-x \
	--with-screen=%{?with_slang:slang}%{!?with_slang:ncurses} \
	%{nil}

#	PYTHON=%{__python3} \
#	--with-gpm-mouse \
#	--disable-rpath \
#

%make_build

%install
%make_install

%__install contrib/mc.{sh,csh} -Dt %{buildroot}%{_sysconfdir}/profile.d

%find_lang %{name} --with-man

%files -f %{name}.lang
%license doc/COPYING
%doc doc/FAQ doc/NEWS doc/README
%{_sysconfdir}/profile.d/*
%dir %{_sysconfdir}/mc
%{_sysconfdir}/mc/edit*
%config(noreplace) %{_sysconfdir}/mc/mc*
%config(noreplace) %{_sysconfdir}/mc/*.ini
%{_bindir}/*
%dir %{_libexecdir}/mc
#%%attr(755,root,root) %%{_libexecdir}/mc/cons.saver
%{_libexecdir}/mc/mc*
%{_libexecdir}/mc/extfs.d
%{_libexecdir}/mc/ext.d
%{_libexecdir}/mc/fish
%{_datadir}/mc
%{_mandir}/man1/*
%exclude %{_libexecdir}/mc/extfs.d/{s3+,uc1541}

#%%files python
#%%{_libexecdir}/mc/extfs.d/{s3+,uc1541}

%changelog
* Sat Oct 10 2020 Daniel Hams <daniel.hams@gmail.com> - 1:4.8.24-3
- Import into sgug-rse. Care with TERM needed, not happy in winterm. python disabled due to dep nightmare.

* Mon Jan 27 2020 Jindrich Novy <jnovy@redhat.com> - 1:4.8.24-3
- be sure to use /var/tmp instead of /tmp (#1795006)

* Mon Jan 20 2020 Jindrich Novy <jnovy@redhat.com> - 1:4.8.24-2
- update to 4.8.24
- drop merged tmpdir patch

* Thu Aug 22 2019 Jindrich Novy <jnovy@redhat.com> - 1:4.8.23-1
- update to 4.8.23
- set the Python path properly as env var, don''t sed the configure directly
