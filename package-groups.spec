Summary:	Mer Package Groups
Name:		package-groups
Version:	0.1
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.merproject.org/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:  libxslt
BuildRequires:  python-yaml
BuildRequires:  python-lxml


%description
Mer Package Groups.

%prep
%setup -q

%build
%ifarch %{arm}
make ARCH=arm
%else
make ARCH=i586
%endif

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/share/package-groups/*xml

